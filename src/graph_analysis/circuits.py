import networkx as nx
import itertools

def find_circuits(G):
    """
    Find all circuits in a directed graph.

    Args:
        G (object): A NetworkX directed graph object

    Returns:
        list: A list of circuits, where each circuit is represented as a list of nodes.
    """

    circuits = []

    if isinstance(G, nx.DiGraph):
        G_undirected = G.to_undirected()
    else:
        G_undirected = G

    for start_node in G_undirected.nodes():
        visited = set()
        edge_used = set()

        def backtrack(node,path,used_edges):
            if len(path) > 1 and path[0] == path[-1]:
                if tuple(path) not in visited:
                    circuits.append(path.copy())
                    visited.add(tuple(path))
                return
        
            for neighbor in G_undirected.neighbors(node):
                edge = tuple(sorted([node, neighbor]))
                if edge not in used_edges:
                    path.append(neighbor)
                    used_edges.add(edge)

                    backtrack(neighbor, path, used_edges)

                    path.pop()
                    used_edges.remove(edge)
        backtrack(start_node, [start_node], edge_used)

        unique_circuits = []
        seen = set()

        for circuit in circuits:
            min_node = min(circuit[:-1])
            min_idx = circuit.index(min_node)
            normalized_circuit = tuple(circuit[min_idx:] + circuit[:min_idx]+ [min_node])

            if normalized_circuit not in seen:
                seen.add(normalized_circuit)
                unique_circuits.append(circuit)

    return unique_circuits

def count_circuits(G):
    """
    Count the number of circuits in a directed graph.

    Args:
        G (object): A NetworkX directed graph object

    Returns:
        int: The number of circuits in the graph.
    """
    return len(find_circuits(G))

def has_eulerian_circuit(G):
    """
    Check if a graph has an Eulerian circuit.
    
    An Eulerian circuit visits every edge exactly once and returns to the starting vertex.
    
    Args:
        G (object): A NetworkX graph object
        
    Returns:
        tuple: (bool, list or None) - (True and the circuit if it exists, False and None otherwise)
    """
    # Check if graph is connected
    if isinstance(G, nx.DiGraph):
        if not nx.is_strongly_connected(G):
            return False, None
        
        # Check if all vertices have equal in and out degree
        for node in G.nodes():
            if G.in_degree(node) != G.out_degree(node):
                return False, None
    else:
        if not nx.is_connected(G):
            return False, None
        
        # Check if all vertices have even degree
        for node, degree in G.degree():
            if degree % 2 != 0:
                return False, None
    
    # Find Eulerian circuit
    try:
        circuit = list(nx.eulerian_circuit(G))
        # Convert edge list to node list
        node_circuit = [circuit[0][0]]
        for edge in circuit:
            node_circuit.append(edge[1])
        return True, node_circuit
    except nx.NetworkXError:
        return False, None

def find_edge_disjoint_circuits(G):
    """
    Find a set of edge-disjoint circuits that cover all edges in the graph.
    
    Args:
        G (object): A NetworkX graph object
        
    Returns:
        list: A list of edge-disjoint circuits, where each circuit is a list of nodes.
    """
    # Make a copy of the graph to work with
    H = G.copy()
    circuits = []
    
    # While there are still edges in the graph
    while H.number_of_edges() > 0:
        # Start from any node with non-zero degree
        for node in H.nodes():
            if H.degree(node) > 0:
                start_node = node
                break
        
        # Build a circuit
        current = start_node
        circuit = [current]
        while True:
            # Find a neighbor
            for neighbor in H.neighbors(current):
                next_node = neighbor
                break
            
            # Remove the edge
            H.remove_edge(current, next_node)
            
            # Move to the next node
            current = next_node
            
            # If we've returned to the start, we've completed a circuit
            if current == start_node:
                circuit.append(current)
                break
            else:
                circuit.append(current)
        
        circuits.append(circuit)
    
    return circuits