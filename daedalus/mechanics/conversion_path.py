

import networkx as nx

class ConversionPath:
    def __init__(self):
        self.graph = nx.DiGraph()

    def define_default(self):
        self.graph.add_edges_from([
            ("Spend", "Impressions"),
            ("Impressions", "Clicks"),
            ("Clicks", "Conversions")
        ])

    def add_edge(self, cause, effect):
        self.graph.add_edge(cause, effect)

    def show_path(self):
        return list(self.graph.edges)

