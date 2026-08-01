"""Figure 14.1: Wexley's existing cloud estate beside the AI-augmented target.

The pairing here is not on-premises against cloud, because the migration is
already done. It is the estate today against the estate with the retrieval path
added, which is the shape of a modernisation question rather than a move.

Run: python diagrams/architecture/fig14_1_wexley.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import Functions, KubernetesEngine
from diagrams.gcp.ml import SpeechToText, VertexAI
from diagrams.gcp.storage import GCS
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Archive Search", "fig14_1_wexley"):
    with Cluster("Today", graph_attr=onprem_cluster_attr()):
        media = GCS("Media in\nCloud Storage")
        ingest = Functions("Ingest events")
        portal = KubernetesEngine("Licensing portal\nGKE")
        media >> ingest

    with Cluster("Added", graph_attr=cloud_cluster_attr()):
        prebuilt = SpeechToText("Prebuilt APIs\ntranscribe and label")
        gen = VertexAI("Generative\ndescription")
        vectors = Server("Vector store")
        prebuilt >> gen >> vectors

    ingest >> Edge(label="new material") >> prebuilt
    media >> Edge(label="backfill as batch", style="dashed") >> prebuilt
    vectors >> Edge(label="cited results") >> portal
