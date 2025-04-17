import networkx as nx
from .generator import generate_random_graph

def check_graph_conditons(G, conditions):
    """
    Check if the graph meets all specified conditions.

    Args:
        G (object): A NetworkX graph object
        conditions (dict)): Dictionary with condition flags
    
    Returns: 
        bool: True if all conditions are met, False otherwise.
        str: Reason for failure if conditions are not met.    
    """

    if conditions.get('must_be_connected', False):
        if not nx.is_connected(G):
            return False, "Graph is not connected."
        
    if conditions.get('all_verticies_even_degree', False):
        degrees = dict(G.degree())
        for node, degree in degrees.items():
            if degree % 2 != 0:
                return False, f"Node {node} has an odd degree."
            
    if conditions.get('must_be_closed', False):
        degrees = dict(G.degree())
        for node, degree in degrees.items():
            if degree == 0:
                return False, f"Node {node} has no edges."
            
    return True, "all conditions met"

def generate_graph_with_conditions(num_nodes, edge_probability, conditions,max_attempts=999):
    """_summary_

    Args:
        num_nodes (int): number of nodes in the graph
        edge_probability (float): probability of creating an edge between any two vertices
        conditions (dict): dictionary with condition flags
           - must_be_connected (bool): whether the graph must be connected
           - all_verticies_even_degree (bool): whether all vertices must have even degree
           - must_be_closed (bool): whether the graph must be closed
        max_attempts (int, optional): Max number of generation attempts: Defaults to 100.

    Returns:
        G (object): A NetworkX graph object that meets the specified conditions
        attempts: number of attempts taken to generate the graph
    """

    for attempt in range(1, max_attempts + 1):
        G = generate_random_graph(num_nodes, edge_probability)
        is_valid, reason = check_graph_conditons(G, conditions)

        if is_valid:
            return G, attempt
        
    return None, max_attempts