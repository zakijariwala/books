"""Figure 16.1: the vehicle fleet and collection tier beside the cloud path.

Draws the three stores as three separate destinations off one pipeline, because
the case study's whole answer is that they serve three different readers and no
one of them substitutes for another.

Run: python diagrams/architecture/fig16_1_ardwick.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.database import Bigtable
from diagrams.gcp.storage import GCS
from diagrams.generic.device import Mobile
from diagrams.onprem.database import Oracle

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Telemetry Path", "fig16_1_ardwick"):
    with Cluster("Fleet and collection tier", graph_attr=onprem_cluster_attr()):
        trucks = Mobile("240,000 units\nbuffer and burst")
        collector = Oracle("Collection tier\nnine terabytes")
        trucks >> collector

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        ps = PubSub("Pub/Sub\nat least once")
        flow = Dataflow("Dataflow\nevent time")
        raw = GCS("Cloud Storage\nretain everything")
        bt = Bigtable("Bigtable\ncounter lookup")
        bq = BigQuery("BigQuery\nfleet analysis")
        ps >> flow
        flow >> raw
        flow >> bt
        flow >> bq

    trucks >> Edge(label="replaces the collection tier") >> ps
