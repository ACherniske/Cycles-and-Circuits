import argparse
from .generator import generate_random_graph
from .analyzer import analyze_graph
from .visualizer import visualize_graph, print_graph_info
from .conditions import generate_graph_with_conditions

def get_user_input():
    """
    Get user input for graph generation and analysis.

    Returns:
        num_nodes (int): Number of nodes in the graph.
        edge_probability (float): Probability of creating an edge between any two vertices.
        conditions (dict): Dictionary with condition flags.
            - must_be_connected (bool): whether the graph must be connected
            - all_verticies_even_degree (bool): whether all vertices must have even degree
            - must_be_closed (bool): whether the graph must be closed
    """

    print("\n=== Graph Generation Parameters ===")

    while True:
        try:
            num_nodes = int(input("Enter the number of nodes (2-100): "))
            if 2 <= num_nodes <= 100:
                break
            print("Please enter a number between 2 and 100.")
        except ValueError:
            print("Please enter a number valid integer.")

    while True:
        try:
            edge_probability = float(input("Enter edge probability (0.0-1.0): "))
            if 0.0 <= edge_probability <= 1.0:
                break
            print("Please enter a number between 0.0 and 1.0.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\n=== Conditions ===")
    print("Select which conditions the graph must satisfy:")

    conditions = {}

    conditions['must_be_connected'] = input("Must be connected? (y/n): ").strip().lower() == 'y'
    conditions['all_verticies_even_degree'] = input("All vertices even degree? (y/n): ").strip().lower() == 'y'
    conditions['must_be_closed'] = input("Must be closed? (y/n): ").strip().lower() == 'y'
    conditions['must_have_hamiltonian'] = input("Must have Hamiltonian cycle? (y/n): ").strip().lower() == 'y'
    return num_nodes, edge_probability, conditions

def main():
    """
    Main function to run the graph generation and analysis with user input.
    """

    print("\n=== Graph Generation and Analysis ===")
    print("This program generates a random graph with specified conditions")

    num_nodes, edge_probability, conditions = get_user_input()

    print("\nGenerating graph...")
    print(f"Conditions: {', '.join([c for c, v in conditions.items() if v])}")

    G, attempts = generate_graph_with_conditions(num_nodes, edge_probability, conditions)

    if G is None:
        print(f"Failed to generate a graph that meets the specified conditions after {attempts} attempts.")
        return
    
    print(f"Graph generated in {attempts} attempts.")

    is_connected, degrees, cycle_count, has_hamiltonian, hamiltonian_cycle = analyze_graph(G)

    visualize_graph(G, is_connected, degrees, hamiltonian_cycle,)

    print_graph_info(is_connected, degrees, cycle_count, has_hamiltonian, hamiltonian_cycle)

    print("\nConditions Met:")
    for condition, is_set in conditions.items():
        if is_set:
            print(f"- {condition.replace('_', ' ').capitalize()}")

    if __name__ == "__main__":
        main()