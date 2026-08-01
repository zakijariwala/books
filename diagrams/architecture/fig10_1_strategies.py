"""Figure 10.1: one application drawn once per migration strategy.

Same application, four targets, so the reader can see what actually changes in
each. Rehost changes the hypervisor. Replatform changes the dependencies.
Refactor changes the application. Repurchase deletes it.

Run: python diagrams/architecture/fig10_1_strategies.py
"""
from diagrams import Cluster, Edge
from diagrams.gcp.compute import ComputeEngine, Run
from diagrams.gcp.database import SQL
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server

from figstyle import cloud_cluster_attr, figure, onprem_cluster_attr

with figure("Four Strategies", "fig10_1_strategies"):
    with Cluster("Today", graph_attr=onprem_cluster_attr()):
        app = Server("Application\nand database")

    with Cluster("Rehost", graph_attr=cloud_cluster_attr()):
        rehost = ComputeEngine("Same app,\nnew hypervisor")

    with Cluster("Replatform", graph_attr=cloud_cluster_attr()):
        replatform = SQL("App unchanged,\nmanaged database")

    with Cluster("Refactor", graph_attr=cloud_cluster_attr()):
        refactor = Run("Rewritten\nservices")

    app >> Edge(label="fastest") >> rehost
    app >> Edge(label="targeted change") >> replatform
    app >> Edge(label="slowest") >> refactor
    app >> Edge(label="repurchase", style="dashed") >> Client("SaaS product")
