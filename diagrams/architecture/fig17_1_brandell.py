"""Figure 17.1: the Brandell monolith beside its target under three strategies.

The book's core device at its purest. The rehost column is what ships before
the lease ends; the refactor column is what the business would prefer and
cannot have by March.

Run: python diagrams/architecture/fig17_1_brandell.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import ComputeEngine, Run
from diagrams.gcp.storage import Filestore, GCS
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Oracle

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Brandell Strategies", "fig17_1_brandell"):
    with Cluster("Leased facility", graph_attr=onprem_cluster_attr()):
        app = Server("Six app servers\nninety batch jobs")
        db = Oracle("Eleven terabytes")
        share = Server("File share\nfour dependants")

    with Cluster("Phase one, by March", graph_attr=cloud_cluster_attr()):
        gce = ComputeEngine("Compute Engine\nrehosted")
        target_db = ComputeEngine("Database, replicated\nthen cut over")
        fs = Filestore("Filestore\ndependency intact")

    with Cluster("Phase two, later", graph_attr=cloud_cluster_attr()):
        later = Run("Services")
        gcs = GCS("Cloud Storage")

    app >> gce
    db >> Edge(label="continuous replication") >> target_db
    share >> fs
    gce >> Edge(label="deliberate debt", style="dashed") >> later
    fs >> Edge(style="dashed") >> gcs
