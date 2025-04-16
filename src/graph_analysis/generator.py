import random
import networkx as nx

def generate_random_graph(num_nodes, edge_probability = 0.5):
    """
    Generate a random graph with num_veritices and random edges

    Args:
        num_nodes (integer): Number of nodes in the graph.
        edge_probability (float, optional): Probability of creating an edge between any two vertices: Defaults to 0.5.

    Returns:
        G: A NetworkX graph object
    """

    G = nx.Graph()

    for i in range(num_nodes):
        G.add_node(i)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                G.add_edge(i, j)

    return G