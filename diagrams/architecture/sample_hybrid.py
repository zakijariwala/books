"""Sample: on-prem node and GCP node in one figure.

Proves the book's core device -- hybrid on-prem/GCP pairing -- renders
grayscale at print spec. Delete once real figures exist; keep the shape.

Run: python diagrams/architecture/sample_hybrid.py
Output: assets/architecture/sample_hybrid.png
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import GCE
from diagrams.gcp.network import LoadBalancing
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Hybrid Connectivity", "sample_hybrid"):
    with Cluster("On-Premises Datacenter", graph_attr=onprem_cluster_attr()):
        app = Server("Application Tier")
        edge_router = Internet("Edge Router")
        app >> edge_router

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        lb = LoadBalancing("Cloud Load Balancing")
        compute = GCE("Compute Engine")
        lb >> compute

    edge_router >> Edge(label="Cloud Interconnect") >> lb
