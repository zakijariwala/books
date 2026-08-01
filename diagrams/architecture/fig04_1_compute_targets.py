"""Figure 4.1: a hypervisor estate beside the compute targets it splits into.

The estate does not migrate as one thing, so the figure shows the split rather
than a one-to-one replacement: what stays a virtual machine, what becomes a
container, and what stops needing a server.

Run: python diagrams/architecture/fig04_1_compute_targets.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import ComputeEngine, Functions, Run
from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Compute Targets", "fig04_1_compute_targets"):
    with Cluster("Hypervisor estate", graph_attr=onprem_cluster_attr()):
        vendor = Server("Vendor appliance\nunchangeable")
        web = LinuxGeneral("Web tier")
        cron = LinuxGeneral("Scheduled job")

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        gce = ComputeEngine("Compute Engine")
        run = Run("Cloud Run")
        func = Functions("Cloud Functions")

    vendor >> Edge(label="rehost") >> gce
    web >> Edge(label="containerise") >> run
    cron >> Edge(label="event handler") >> func
