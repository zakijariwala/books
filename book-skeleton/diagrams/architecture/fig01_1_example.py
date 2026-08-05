"""Figure 1.1: an example architecture figure. Replace with your own.

The convention every architecture figure follows:

- One source file per figure, named figNN_M_slug to match its `Figure N.M`
  caption in the manuscript (chapter N, figure M).
- Import `figure` from figstyle so grayscale, DPI, and the 4.5in text-block
  width are applied for you and enforced on exit.
- Use the grayscale cluster fills, never colour: the interior prints black and
  white and a colour-coded legend is invisible in it.

A common and effective device is a "before beside after" pairing in one figure
-- the old system on the left, the new one on the right -- so the reader sees
the delta at a glance. Keep labels terse: a 4.5in-wide figure holds about two
columns of short labels before its type drops below the 8pt print floor that
normalize_image.py enforces.

Run: python diagrams/architecture/fig01_1_example.py
"""
from diagrams import Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.onprem.client import Users

from figstyle import figure, left_cluster_attr, right_cluster_attr

with figure("Before and After", "fig01_1_example", direction="LR"):
    with Cluster("Before", graph_attr=left_cluster_attr()):
        team = Users("Team")
        old = Rack("Manual\nprocess")
        team >> old

    with Cluster("After", graph_attr=right_cluster_attr()):
        new = Rack("Automated\npipeline")
        store = Storage("Output")
        new >> store

    old >> Edge(label="migrate", style="dashed") >> new
