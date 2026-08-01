"""Figure 6.1: block, file, object, and relational storage and their targets.

One row per storage kind, so the reader can see that the SAN and the filer have
different answers and that the filer's answer depends on whether the
application can be changed.

Run: python diagrams/architecture/fig06_1_storage_map.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.database import SQL
from diagrams.gcp.storage import Filestore, GCS, PersistentDisk
from diagrams.generic.storage import Storage
from diagrams.onprem.database import Mysql

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Storage Mapping", "fig06_1_storage_map"):
    with Cluster("Datacentre", graph_attr=onprem_cluster_attr()):
        san = Storage("SAN\nblock")
        filer = Storage("NFS filer\nfile")
        db = Mysql("Relational")

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        pd = PersistentDisk("Persistent Disk")
        fs = Filestore("Filestore")
        gcs = GCS("Cloud Storage")
        sql = SQL("Cloud SQL")

    san >> pd
    filer >> Edge(label="app unchanged") >> fs
    filer >> Edge(label="app rewritten", style="dashed") >> gcs
    db >> sql
