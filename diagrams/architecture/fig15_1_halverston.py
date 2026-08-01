"""Figure 15.1: the Halverston estate beside its target, with the approval gate.

The gate is drawn on the path to the public site rather than off to one side,
because that is the whole point: nothing reaches the catalogue without passing
through it.

Run: python diagrams/architecture/fig15_1_halverston.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.compute import KubernetesEngine
from diagrams.gcp.database import SQL
from diagrams.gcp.ml import VisionAPI
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mssql

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Halverston Target", "fig15_1_halverston"):
    with Cluster("On-premises", graph_attr=onprem_cluster_attr()):
        orders = Mssql("Order management\nin card scope")
        sftp = Server("Nightly supplier\nfile exchange")

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        events = PubSub("Pub/Sub\nstock updates")
        catalogue = SQL("Cloud SQL\nconsolidated")
        vision = VisionAPI("Attributes\nand drafts")
        store = KubernetesEngine("Storefront\nautoscaled")

    review = User("Merchandiser\napproval")

    sftp >> Edge(label="replaces the batch window") >> events >> catalogue
    vision >> Edge(label="review queue") >> review >> Edge(label="published") >> store
    orders >> Edge(label="stays put this phase", style="dashed") >> catalogue
