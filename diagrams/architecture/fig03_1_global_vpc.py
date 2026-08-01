"""Figure 3.1: VLANs and MPLS beside a global VPC with regional subnets.

Draws the regional boundary in each model. On-premises the boundary is the
site; on Google Cloud the VPC spans regions and the subnet is the regional
object, which is the habit AWS architects have to unlearn.

Run: python diagrams/architecture/fig03_1_global_vpc.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.network import DedicatedInterconnect, VirtualPrivateCloud
from diagrams.generic.network import Router, Subnet
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Global VPC", "fig03_1_global_vpc"):
    with Cluster("Datacentre", graph_attr=onprem_cluster_attr()):
        vlan = Subnet("VLAN per tier")
        mpls = Router("MPLS to colo")
        Server("Application") >> vlan >> mpls

    with Cluster("Google Cloud, one VPC", graph_attr=cloud_cluster_attr()):
        vpc = VirtualPrivateCloud("Global VPC")
        eu = Subnet("Subnet\neurope-west2")
        us = Subnet("Subnet\nus-central1")
        vpc >> eu
        vpc >> us
        eu >> Edge(label="private, no peering") >> us

    mpls >> Edge(label="Interconnect") >> DedicatedInterconnect("Attachment") >> vpc
