import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, is_connected, degrees, output_path=None):
    """
    Visualize the graph and display connectivity and degree information

    Args:
        G (object): A NetworkX graph object
        is_connected (bool): Boolean indicating if the graph is connected
        degrees (dict): A dictionary of vertex degrees
        output_path (path, optional): Optional path to save the graph image: Defaults to None.

    Returns:
        None
    """
    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', width=1, alpha=0.7)

    if is_connected:
        plt.title("Connected Graph", fontsize=16)
    else:
        plt.title("Disconnected Graph", fontsize=16)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        plt.close()
    else:
        plt.show()

def print_degree_info(is_connected, degrees):
    """
    Print the degree information of the graph

    Args:
        is_connected (bool): Boolean indicating if the graph is connected
        degrees (dict): A dictionary of vertex degrees

    Returns:
        None
    """
    print(f"Graph is {'connected' if is_connected else 'disconnected'}")
    print("\nVertex Degrees:")
    for node, degree in sorted(degrees.items()):
        print(f"Node {node}: Degree {degree}")

    min_degree = min(degrees.values())
    max_degree = max(degrees.values())
    avg_degree = sum(degrees.values()) / len(degrees)

    print(f"\nMinimum Degree: {min_degree}")
    print(f"Maximum Degree: {max_degree}")
    print(f"Average Degree: {avg_degree:.2f}")