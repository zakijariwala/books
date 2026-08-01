"""Figure 13.1: the Northmoor estate beside its target, one service at a time.

Deliberately drawn service by service, because the chapter's answer is that
different components take different strategies. The records system stays a
virtual machine while everything around it becomes managed.

Run: python diagrams/architecture/fig13_1_northmoor.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import ComputeEngine, KubernetesEngine
from diagrams.gcp.database import Memorystore, SQL
from diagrams.gcp.storage import GCS
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mssql, Mysql

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Northmoor Target", "fig13_1_northmoor"):
    with Cluster("Co-location facility", graph_attr=onprem_cluster_attr()):
        records = Mssql("Clinical records\nvendor supported")
        portal = Mysql("Laboratory portal")
        cache = Server("Redis")
        docs = Server("Scanned referrals\non a filer")

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        gce = ComputeEngine("Compute Engine\nif versions unmanaged")
        sql = SQL("Cloud SQL")
        mem = Memorystore("Memorystore")
        gcs = GCS("Cloud Storage\nlifecycle rules")
        gke = KubernetesEngine("Regional GKE\neleven services")

    records >> Edge(label="support matrix decides") >> gce
    portal >> sql
    cache >> mem
    docs >> gcs
