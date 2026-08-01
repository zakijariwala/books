"""Sample: on-prem node and GCP node in one figure.

Proves the book's core device — hybrid on-prem/GCP pairing — renders
grayscale at print-safe resolution before any other diagram work happens.

Run: python diagrams/architecture/sample_hybrid.py
Output: assets/architecture/sample_hybrid.png
"""
import os

from diagrams import Diagram, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.onprem.network import Internet

OUT_DIR = os.path.join("assets", "architecture")
os.makedirs(OUT_DIR, exist_ok=True)

# Grayscale / high-contrast graph attrs for KDP black-and-white interior.
# Trim size 6x9in, usable width ~4.5in -> at 300 DPI ~1350px wide.
GRAPH_ATTR = {
    "bgcolor": "white",
    "fontname": "Helvetica",
    "fontcolor": "black",
    "dpi": "300",
    "size": "4.5",
    "ratio": "compress",
}
NODE_ATTR = {
    "fontname": "Helvetica",
    "fontcolor": "black",
    "color": "black",
    "style": "filled",
    "fillcolor": "white",
}
EDGE_ATTR = {
    "color": "black",
    "fontname": "Helvetica",
    "fontcolor": "black",
}

with Diagram(
    "Sample Hybrid Architecture",
    filename=os.path.join(OUT_DIR, "sample_hybrid"),
    show=False,
    outformat="png",
    graph_attr=GRAPH_ATTR,
    node_attr=NODE_ATTR,
    edge_attr=EDGE_ATTR,
):
    onprem = Internet("On-Prem Datacenter")
    gcp_lb = LoadBalancing("GCP Load Balancer")

    onprem >> Edge(label="VPN Tunnel", color="black", fontcolor="black") >> gcp_lb
