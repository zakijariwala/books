"""Figure 5.1: a self-managed cluster beside GKE Standard and Autopilot.

The figure is about ownership, not features: which components you keep running
in each mode. That is what decides the cost model and the Saturday upgrades.

Run: python diagrams/architecture/fig05_1_gke_ownership.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import KubernetesEngine
from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Who Owns What", "fig05_1_gke_ownership"):
    with Cluster("Self-managed", graph_attr=onprem_cluster_attr()):
        cp = Server("Control plane\nyours")
        nodes = LinuxGeneral("Nodes\nyours")
        cp >> nodes

    with Cluster("GKE Standard", graph_attr=cloud_cluster_attr()):
        std_cp = KubernetesEngine("Control plane\nGoogle")
        std_nodes = LinuxGeneral("Nodes\nyours")
        std_cp >> std_nodes

    with Cluster("GKE Autopilot", graph_attr=cloud_cluster_attr()):
        auto = KubernetesEngine("Control plane\nand nodes\nGoogle")

    nodes >> Edge(label="hand over the plane") >> std_cp
    std_nodes >> Edge(label="hand over the nodes") >> auto
