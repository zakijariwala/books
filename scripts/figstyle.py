"""Shared figure style for every architecture diagram in the book.

Import this rather than setting Graphviz attributes per script. Forty figures
copy-pasting print constraints is forty chances to drift out of KDP spec.

    from figstyle import figure
    from diagrams.gcp.compute import GCE
    from diagrams.onprem.compute import Server

    with figure("Hybrid Compute", "hybrid_compute"):
        Server("On-Prem") >> GCE("Compute Engine")

Print constraints enforced here, not by hand and not as a post-processing step:

- KDP paperback interior prints black and white, so everything renders
  grayscale. No color, no color-coded legends.
- Trim size 6x9in with 0.875in inside and 0.625in outside margins leaves a
  4.5in text block. Figures render to fill it exactly.
- 4.5in at 300 DPI is 1350px. Output is normalized to that on exit.

Reachable on sys.path because the Makefile sets PYTHONPATH=scripts. Note that
this file must NOT live in the repo's diagrams/ directory: that would shadow
the installed `diagrams` package.
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
# distinguish on-prem from cloud, or one zone from another. Anything that
# relies on hue is unreadable once KDP prints it.
FILL_ONPREM = "#e8e8e8"
FILL_CLOUD = "#f7f7f7"
FILL_EMPHASIS = "#d0d0d0"

ARCH_OUT_DIR = os.path.join("assets", "architecture")


@contextmanager
def figure(title, slug, out_dir=ARCH_OUT_DIR, direction="LR"):
    """Render one figure to out_dir/slug.png at KDP print spec.

    title    caption drawn inside the image
    slug     output filename stem, matching the source script's name
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


def onprem_cluster_attr():
    """Graphviz attributes for an on-premises cluster box."""
    return {"bgcolor": FILL_ONPREM, "fontname": "Helvetica", "fontcolor": "black"}


def cloud_cluster_attr():
    """Graphviz attributes for a Google Cloud cluster box."""
    return {"bgcolor": FILL_CLOUD, "fontname": "Helvetica", "fontcolor": "black"}
