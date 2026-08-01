"""Figure 11.1: an active-passive DR pair beside a multi-region topology.

Marks where RTO and RPO are actually decided, which is at the replication link
rather than at the standby site. The untested restore on the left is the point
of the figure.

Run: python diagrams/architecture/fig11_1_dr_topology.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.network import LoadBalancing
from diagrams.generic.place import Datacenter
from diagrams.generic.storage import Storage

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("DR Topology", "fig11_1_dr_topology"):
    with Cluster("Active-passive pair", graph_attr=onprem_cluster_attr()):
        primary = Datacenter("Primary site")
        standby = Datacenter("Standby site")
        tape = Storage("Backups\nrestore untested")
        primary >> Edge(label="RPO decided here") >> standby
        primary >> tape

    with Cluster("Multi-region", graph_attr=cloud_cluster_attr()):
        lb = LoadBalancing("Global load\nbalancer")
        r1 = ComputeEngine("Region A")
        r2 = ComputeEngine("Region B")
        lb >> r1
        lb >> r2
        r1 >> Edge(label="replication", style="dashed") >> r2

    standby >> Edge(label="RTO is unknown until tested") >> lb
