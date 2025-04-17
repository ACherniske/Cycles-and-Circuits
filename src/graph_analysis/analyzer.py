import networkx as nx 
from .cycles import count_cycles, has_hamiltonian_cycle

def analyze_graph(G):
    """
    Analyze the graph for connectivity and vertex degrees

    Args:
        G (object): A NetworkX graph object

    Returns:
        is_connected: Boolean indicating if the graph is connected
        degrees: List of vertex degrees
    """

    is_connected = nx.is_connected(G)

    degrees = dict(G.degree())

    cycle_count = count_cycles(G)

    has_hamiltonian, hamiltonian_cycle = has_hamiltonian_cycle(G)

    return is_connected, degrees, cycle_count, has_hamiltonian, hamiltonian_cycle

def calculate_degree_statistics(degrees):
    """
    Calculate statistics about vertex degrees.

    Args:
        degrees (dict): A dictionary of vertex degrees
    
    Returns:
        Statistics including min, max, and average degree.
    """

    min_degree = min(degrees.values())
    max_degree = max(degrees.values())
    avg_degree = sum(degrees.values()) / len(degrees)

    return {
            "min_degree": min_degree,
            "max_degree": max_degree,
            "avg_degree": avg_degree
    }