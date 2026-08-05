"""Shared figure style for every architecture diagram in the book.

Import this rather than setting Graphviz attributes per script. A dozen figures
copy-pasting print constraints is a dozen chances to drift out of print spec.

    from figstyle import figure, left_cluster_attr, right_cluster_attr
    from diagrams.generic.compute import Rack
    from diagrams.onprem.client import Users

    with figure("Before and After", "fig01_1_example"):
        Users("Team") >> Rack("System")

Print constraints enforced here, not by hand and not as a post-processing step:

- A print interior is black and white, so everything renders grayscale. No
  colour, no colour-coded legends.
- Trim size 6x9in with a 0.875in inside and 0.625in outside margin leaves a
  4.5in text block. Figures render to fill it exactly.
- 4.5in at 300 DPI is 1350px. Output is normalized to that on exit.

Reachable on sys.path because the Makefile sets PYTHONPATH=scripts. Note that
this file must NOT live in the repo's diagrams/ directory: that would shadow
the installed `diagrams` package.

The `diagrams` library ships node sets for many vendors (generic, onprem, aws,
azure, gcp, k8s, programming, saas...). Import whichever fit your subject; the
style below is vendor-neutral and forces every node to the same grayscale look.
"""
import os
from contextlib import contextmanager

from diagrams import Diagram

from normalize_image import normalize

# 6x9in trim, 0.875in inside margin, 0.625in outside margin.
TEXT_BLOCK_INCHES = 4.5
PRINT_DPI = 300

GRAPH_ATTR = {
    "bgcolor": "white",
    "fontname": "Helvetica",
    "fontcolor": "black",
    "dpi": str(PRINT_DPI),
    "size": str(TEXT_BLOCK_INCHES),
    "ratio": "compress",
    "pad": "0.2",
    "nodesep": "0.6",
    "ranksep": "0.8",
}

NODE_ATTR = {
    "fontname": "Helvetica",
    "fontcolor": "black",
    "color": "black",
    "style": "filled",
    "fillcolor": "white",
    "fontsize": "13",
}

EDGE_ATTR = {
    "color": "black",
    "fontname": "Helvetica",
    "fontcolor": "black",
    "fontsize": "11",
}

# Grayscale fills for cluster backgrounds. Use these instead of colour to
# distinguish one grouping from another -- before from after, old from new,
# system A from system B. Anything that relies on hue is unreadable in print.
FILL_LEFT = "#e8e8e8"
FILL_RIGHT = "#f7f7f7"
FILL_EMPHASIS = "#d0d0d0"

ARCH_OUT_DIR = os.path.join("assets", "architecture")


@contextmanager
def figure(title, slug, out_dir=ARCH_OUT_DIR, direction="LR"):
    """Render one figure to out_dir/slug.png at print spec.

    title      caption drawn inside the image
    slug       output filename stem, matching the source script's name
    direction  "LR" reads better than "TB" inside a 4.5in text block
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, slug)

    with Diagram(
        title,
        filename=path,
        show=False,
        outformat="png",
        direction=direction,
        graph_attr=GRAPH_ATTR,
        node_attr=NODE_ATTR,
        edge_attr=EDGE_ATTR,
    ):
        yield

    # Normalize here, not in the Makefile, so a figure rendered directly while
    # iterating still comes out at print spec.
    normalize(f"{path}.png")


def left_cluster_attr():
    """Graphviz attributes for the left / "before" cluster box."""
    return {"bgcolor": FILL_LEFT, "fontname": "Helvetica", "fontcolor": "black"}


def right_cluster_attr():
    """Graphviz attributes for the right / "after" cluster box."""
    return {"bgcolor": FILL_RIGHT, "fontname": "Helvetica", "fontcolor": "black"}
