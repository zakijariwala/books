"""Print-spec enforcement for rendered figures.

The rules being protected: a figure fits the 4.5x7in text block, prints
grayscale because the interior is black and white, and fails the build when its
type would come out too small to read. Each of these has already been wrong
once.
"""
import pytest
from PIL import Image

from normalize_image import (
    MAX_HEIGHT,
    MIN_PRINT_PT,
    SCALE_KEY,
    TARGET_DPI,
    TARGET_WIDTH,
    normalize,
    print_point_size,
)


def write_png(path, width, height, mode="RGB", colour=(200, 30, 30)):
    Image.new(mode, (width, height), colour).save(path)
    return path


def test_wide_figure_is_scaled_down_to_the_measure(tmp_path):
    p = write_png(tmp_path / "wide.png", 2700, 1000)
    normalize(p)
    assert Image.open(p).width == TARGET_WIDTH


def test_narrow_figure_is_scaled_up_to_fill_the_measure(tmp_path):
    # Graphviz renders small. Leaving it small would waste the page and shrink
    # nothing but the type, so the fit works in both directions.
    p = write_png(tmp_path / "narrow.png", 400, 300)
    normalize(p)
    assert Image.open(p).width == TARGET_WIDTH


def test_tall_figure_is_capped_by_height_not_width(tmp_path):
    # The bug this protects: enforcing width alone let a figure come out 14in
    # tall on a 9in page.
    p = write_png(tmp_path / "tall.png", 1000, 4000)
    normalize(p)
    im = Image.open(p)
    assert im.height == MAX_HEIGHT
    assert im.width < TARGET_WIDTH


def test_aspect_ratio_is_preserved(tmp_path):
    p = write_png(tmp_path / "ratio.png", 800, 1200)
    before = 800 / 1200
    normalize(p)
    im = Image.open(p)
    assert im.width / im.height == pytest.approx(before, rel=0.01)


def test_output_is_grayscale(tmp_path):
    # The interior prints black and white. A colour figure that only reads in
    # colour should look wrong here rather than at the printer.
    p = write_png(tmp_path / "colour.png", 1350, 900, colour=(255, 0, 0))
    normalize(p)
    assert Image.open(p).mode == "L"


def test_dpi_metadata_is_set_for_print(tmp_path):
    # PNG stores resolution as integer pixels per metre, so 300 dpi round-trips
    # as 299.9994. That rounding is why figures capped at 7in measure 7.02in in
    # the built DOCX; it is harmless, but it has to be read approximately.
    p = write_png(tmp_path / "dpi.png", 1350, 900)
    normalize(p)
    assert Image.open(p).info["dpi"] == pytest.approx(TARGET_DPI, rel=1e-5)


def test_scale_is_recorded_in_the_png(tmp_path):
    p = write_png(tmp_path / "scale.png", 675, 400)
    scale = normalize(p)
    assert float(Image.open(p).text[SCALE_KEY]) == pytest.approx(scale)


def test_second_run_reports_the_same_scale(tmp_path):
    # Regression: the legibility check recomputed 1.0 against the already
    # fitted image and declared every figure legible on re-runs.
    p = write_png(tmp_path / "idem.png", 2700, 1000)
    first = normalize(p)
    assert normalize(p) == pytest.approx(first)


def test_second_run_does_not_resize_again(tmp_path):
    p = write_png(tmp_path / "idem2.png", 2700, 1000)
    normalize(p)
    size = Image.open(p).size
    normalize(p)
    assert Image.open(p).size == size


def test_point_size_falls_with_scale():
    assert print_point_size(1.0) > print_point_size(0.5)


def test_a_dense_figure_fails_the_legibility_floor():
    # A figure so wide it must be shrunk hard is the signal to simplify the
    # figure, not to enlarge the image: the page size is fixed.
    heavily_shrunk = 0.2
    assert print_point_size(heavily_shrunk) < MIN_PRINT_PT
