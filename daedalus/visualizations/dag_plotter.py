import matplotlib.pyplot as plt
import networkx as nx

def plot_dag(graph, title="Causal Graph"):
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, arrows=True)
    nx.draw_networkx_edge_labels(graph, pos)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
