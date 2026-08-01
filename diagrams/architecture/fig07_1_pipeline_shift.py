"""Figure 7.1: nightly batch ETL and Hadoop beside the managed pipeline.

The left side is a chain with a window that either finishes by 06:00 or does
not. The right side separates ingest, processing, and analysis so the batch
window stops being the design.

Run: python diagrams/architecture/fig07_1_pipeline_shift.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.storage import GCS
from diagrams.onprem.analytics import Hadoop
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Batch to Managed Pipeline", "fig07_1_pipeline_shift"):
    with Cluster("Nightly batch", graph_attr=onprem_cluster_attr()):
        sftp = Server("SFTP drop")
        hadoop = Hadoop("Hadoop cluster\nsized for peak")
        sftp >> Edge(label="scheduler") >> hadoop

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        pubsub = PubSub("Pub/Sub")
        flow = Dataflow("Dataflow")
        raw = GCS("Cloud Storage\nraw capture")
        bq = BigQuery("BigQuery")
        pubsub >> flow >> bq
        flow >> raw

    sftp >> Edge(label="continuous ingest") >> pubsub
    hadoop >> Edge(label="lift jobs to Dataproc", style="dashed") >> flow
