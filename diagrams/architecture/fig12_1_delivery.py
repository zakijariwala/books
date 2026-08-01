"""Figure 12.1: ticket-driven manual provisioning beside a pipeline.

Configuration drift on the left is drawn as two environments built eighteen
months apart. On the right the same module produces both, which is the actual
remedy for staging passing while production fails.

Run: python diagrams/architecture/fig12_1_delivery.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import BinaryAuthorization
from diagrams.gcp.devtools import Build
from diagrams.gcp.storage import GCS
from diagrams.onprem.client import User
from diagrams.onprem.iac import Terraform

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Manual to Pipeline", "fig12_1_delivery"):
    with Cluster("Ticket driven", graph_attr=onprem_cluster_attr()):
        eng = User("Engineer\nand a wiki page")
        staging = GCS("Staging\nbuilt by hand")
        prod = GCS("Production\nbuilt differently")
        eng >> staging
        eng >> prod

    with Cluster("Codified", graph_attr=cloud_cluster_attr()):
        tf = Terraform("One module,\nper-environment\nvariables")
        state = GCS("Remote state\nversioned bucket")
        build = Build("Cloud Build\nand Cloud Deploy")
        gate = BinaryAuthorization("Approval and\nBinary Authorization")
        tf >> state
        tf >> build >> gate

    prod >> Edge(label="drift ends here", style="dashed") >> tf
