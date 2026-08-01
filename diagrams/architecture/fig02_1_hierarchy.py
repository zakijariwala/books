"""Figure 2.1: an AD forest and OU tree beside the Google Cloud hierarchy.

The point of the pairing is that the organization, folder, project chain has no
AWS or Azure equivalent, so the reader needs the shape of it before anything
downstream references a project.

Run: python diagrams/architecture/fig02_1_hierarchy.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.security import ResourceManager
from diagrams.generic.place import Datacenter
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Resource Hierarchy", "fig02_1_hierarchy", direction="TB"):
    with Cluster("Active Directory", graph_attr=onprem_cluster_attr()):
        forest = Datacenter("Forest")
        ou = Server("Organizational\nUnit")
        staff = Users("Users and\ngroups")
        forest >> ou >> staff

    with Cluster("Google Cloud", graph_attr=cloud_cluster_attr()):
        org = ResourceManager("Organization")
        folder = ResourceManager("Folder")
        project = ResourceManager("Project")
        org >> folder >> project

    ou >> Edge(label="federated identity", style="dashed") >> folder
