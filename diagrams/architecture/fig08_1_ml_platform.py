"""Figure 8.1: GPU workstations and a pickle file beside the managed lifecycle.

The left side is where most data science estates actually are. The right side
exists to answer governance questions -- which data trained this, which version
is deployed -- rather than to train faster.

Run: python diagrams/architecture/fig08_1_ml_platform.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.ml import AIPlatform, VertexAI
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("ML Lifecycle", "fig08_1_ml_platform"):
    with Cluster("Under the desks", graph_attr=onprem_cluster_attr()):
        ws = Server("GPU workstation\nnotebooks")
        share = Storage("Shared drive\nmodel.pkl")
        ws >> Edge(label="hand off") >> share

    with Cluster("Vertex AI", graph_attr=cloud_cluster_attr()):
        train = VertexAI("Training")
        registry = AIPlatform("Model Registry\nand lineage")
        serve = AIPlatform("Batch or\nonline prediction")
        train >> registry >> serve

    share >> Edge(label="no reproducibility", style="dashed") >> train
