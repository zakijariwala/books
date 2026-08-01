"""Figure 9.1: the on-premises perimeter beside the layered cloud model.

Shows where the perimeter concept survives and where it does not. The firewall
still governs reachability; it does not govern an authorised user copying data
out, which is the layer VPC Service Controls occupies.

Run: python diagrams/architecture/fig09_1_perimeter.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.security import IAP, KMS, SecurityCommandCenter
from diagrams.generic.network import Firewall
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Perimeter to Layers", "fig09_1_perimeter"):
    with Cluster("One hard perimeter", graph_attr=onprem_cluster_attr()):
        fw = Firewall("Firewall")
        trusted = Server("Trusted inside")
        fw >> trusted

    with Cluster("Layered controls", graph_attr=cloud_cluster_attr()):
        iap = IAP("Identity-Aware Proxy\nand context")
        perimeter = SecurityCommandCenter("Service perimeter\nblocks exfiltration")
        kms = KMS("CMEK\nkey control")
        iap >> perimeter >> kms

    Users("Staff") >> Edge(label="no implicit trust") >> iap
    trusted >> Edge(label="perimeter alone is not enough", style="dashed") >> perimeter
