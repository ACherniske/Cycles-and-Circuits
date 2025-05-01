import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, is_connected, degrees, hamiltonian_cycle=None, eulerian_circuit=None, output_path=None):
    """
    Visualize the graph and display connectivity and degree information

    Args:
        G (object): A NetworkX graph object
        is_connected (bool): Boolean indicating if the graph is connected
        degrees (dict): A dictionary of vertex degrees
        hamiltonian_cycle (list, optional): List of nodes forming a Hamiltonian cycle
        eulerian_circuit (list, optional): List of nodes forming an Eulerian circuit
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
                              width=2.5, edge_color='red', style='dotted', alpha=0.8)

    if eulerian_circuit and len(eulerian_circuit) > 1:
        print(f"Eulerian circuit nodes: {eulerian_circuit}")
        eulerian_edges = []
        for i in range(len(eulerian_circuit) - 1):
            source = eulerian_circuit[i]
            target = eulerian_circuit[i + 1]
            # Ensure the edge exists in the graph
            if G.has_edge(source, target):
                eulerian_edges.append((source, target))
            else:
                print(f"Warning: Edge ({source}, {target}) not found in graph")
        
        print(f"Eulerian edges to draw: {eulerian_edges}")
        if eulerian_edges:  # Only draw if we have valid edges
            nx.draw_networkx_edges(G, pos, edgelist=eulerian_edges, 
                                width=2.0, edge_color='green', alpha=0.8)

    title = "Connected Graph" if is_connected else "Disconnected Graph"
    if hamiltonian_cycle:
        title += " (Has Hamiltonian Cycle)"
    if eulerian_circuit:
        title += " (Has Eulerian Circuit)"
    plt.title(title, fontsize=16)

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        plt.close()
    else:
        plt.show()

def print_graph_info(is_connected, degrees, cycle_count, circuit_count, has_hamiltonian, has_eulerian, hamiltonian_cycle=None, eulerian_circuit=None):
    """
    Print information about the graph

    Args:
        is_connected (bool): Boolean indicating if the graph is connected
        degrees (dict): A dictionary of vertex degrees
        cycle_count (int): Number of cycles in the graph
        has_hamiltonian (bool): Boolean indicating if the graph has a Hamiltonian cycle
        has_eulerian (bool): Boolean indicating if the graph has an Eulerian circuit
        hamiltonian_cycle (list, optional): List of nodes forming a Hamiltonian cycle
        eulerian_circuit (list, optional): List of nodes forming an Eulerian circuit

    Returns:
        None
    """
    print(f"Graph is {'connected' if is_connected else 'disconnected'}")
    print(f"Total number of cycles: {cycle_count}")
    print(f"Total number of circuits: {circuit_count}")
    print(f"Has Hamiltonian cycle: {'Yes' if has_hamiltonian else 'No'}")
    print(f"Has Eulerian circuit: {'Yes' if has_eulerian else 'No'}")
    
    if hamiltonian_cycle:
        cycle_str = " → ".join(str(v) for v in hamiltonian_cycle)
        print(f"Hamiltonian cycle: {cycle_str} → {hamiltonian_cycle[0]}")
        
    if eulerian_circuit:
        circuit_str = " → ".join(str(v) for v in eulerian_circuit)
        print(f"Eulerian circuit: {circuit_str}")

    min_degree = min(degrees.values())
    max_degree = max(degrees.values())
    avg_degree = sum(degrees.values()) / len(degrees)

    print(f"\nMinimum Degree: {min_degree}")
    print(f"Maximum Degree: {max_degree}")
    print(f"Average Degree: {avg_degree:.2f}")