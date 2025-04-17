import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, is_connected, degrees, hamiltonian_cycle=None, output_path=None):
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

    if hamiltonian_cycle:
        hamiltonian_edges = list(zip(hamiltonian_cycle, hamiltonian_cycle[1:] + [hamiltonian_cycle[0]]))
        nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges, 
                              width=2.5, edge_color='red', alpha=0.8)

    title = "Connected Graph" if is_connected else "Disconnected Graph"
    if hamiltonian_cycle:
        title += " (Has Hamiltonian Cycle)"
    plt.title(title, fontsize=16)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        plt.close()
    else:
        plt.show()

def print_graph_info(is_connected, degrees, cycle_count, has_hamiltonian, hamiltonian_cycle=None):
    """
    Print the degree information of the graph

    Args:
        is_connected (bool): Boolean indicating if the graph is connected
        degrees (dict): A dictionary of vertex degrees

    Returns:
        None
    """
    print(f"Graph is {'connected' if is_connected else 'disconnected'}")
    print(f"Total number of cycles: {cycle_count}")
    print(f"Has Hamiltonian cycle: {'Yes' if has_hamiltonian else 'No'}")
    
    if hamiltonian_cycle:
        cycle_str = " → ".join(str(v) for v in hamiltonian_cycle)
        print(f"Hamiltonian cycle: {cycle_str} → {hamiltonian_cycle[0]}")

    """
    # commented out for cleaner output
    print("\nVertex Degrees:")
    for node, degree in sorted(degrees.items()):
        print(f"Node {node}: Degree {degree}")
    """

    min_degree = min(degrees.values())
    max_degree = max(degrees.values())
    avg_degree = sum(degrees.values()) / len(degrees)

    print(f"\nMinimum Degree: {min_degree}")
    print(f"Maximum Degree: {max_degree}")
    print(f"Average Degree: {avg_degree:.2f}")