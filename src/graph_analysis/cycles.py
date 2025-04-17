import networkx as nx
import itertools

def find_cycles(G):
    """
    Find all cycles in a graph.

    Args:
        G (object): A NetworkX graph object

    Returns:
        list: A list of cycles, where each cycle is represented as a list of nodes.
    """
    return list(nx.simple_cycles(nx.DiGraph))

def count_cycles(G):
    """
    Count the number of cycles in a graph.

    Args:
        G (object): A NetworkX graph object

    Returns:
        int: The number of cycles in the graph.
    """
    if isinstance(G, nx.DiGraph):
        # Each undirected edge becomes two directed edges
        DG = nx.DiGraph(G)
        for u, v in G.edges():
            DG.add_edge(v, u)
            DG.add_edge(u, v)
        cycles = list(nx.simple_cycles(DG))

        unique_cycles = set()
        for cycle in cycles:
            min_idx = cycle.index(min(cycle))
            normalized_cycle = tuple((cycle[min_idx:] + cycle[:min_idx]))
            reversed_cycle = tuple(reversed(normalized_cycle))

        if normalized_cycle not in unique_cycles and reversed_cycle not in unique_cycles:
            unique_cycles.add(normalized_cycle)

        return len(unique_cycles)
    else:
        return len(list(nx.simple_cycles(G)))
    
def has_hamiltonian_cycle(G):
    """
    Check if a graph has a Hamiltonian cycle.

    Args:
        G (object): A NetworkX graph object

    Returns:
        bool: True if the graph has a Hamiltonian cycle, False otherwise.
    """
    if not nx.is_connected(G):
        return False,None
    for node, degree in G.degree():
        if degree < 2:
            return False,None
    
    n = len(G.nodes)
    if n <= 20:
        nodes = list(G.nodes)
        for perm in itertools.permutations(nodes):
            is_cycle = True
            for i in range(n-1):
                if not G.has_edge(perm[i], perm[i+1]):
                    is_cycle = False
                    break
            if is_cycle and G.has_edge(perm[n-1], perm[0]):
                return True,list(perm)
        return False,None
    else:
        try:
            cycle = nx.approximation.traveling_salesman_problem(G, cycle=True)
            if len(cycle) == n + 1 and cycle[0] == cycle[-1]:
                for i in range (n):
                    if not G.has_edge(cycle[i], cycle[i+1]):
                        return False,None
                return True,cycle[:-1]
        except:
            return False,None

