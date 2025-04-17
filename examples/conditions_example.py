from graph_analysis import generate_graph_with_conditions, analyze_graph, visualize_graph

def main():

    num_nodes = 10
    edge_probability = 0.3

    conditions = {
        'must_be_connected': True,
        'all_verticies_even_degree': True,
        'must_be_closed': True
    }

print(f"Generating graph with conditions:")
for condition, value in conditions.items():
    print(f" - {condition}")

G, attempts = generate_graph_with_conditions(num_nodes, edge_probability, conditions)

if G is None:
    print(f"Failed to generate a graph that meets the specified conditions after {attempts} attempts.")

print(f"Graph generated in {attempts} attempts.")

is_connected, degrees = analyze_graph(G)

visualize_graph(G, is_connected, degrees)

if __name__ == "__main__":
    main()