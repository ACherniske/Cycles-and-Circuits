from graph_analysis import generate_random_graph, analyze_graph, visualize_graph
from graph_analysis.analyzer import calculate_degree_statistics

def main():
    num_vertices = 10
    edge_probability = 0.3

    G = generate_random_graph(num_vertices, edge_probability)

    is_connected, degrees = analyze_graph(G)

    stats = calculate_degree_statistics(degrees)

    print(f"Graph is {'connected' if is_connected else 'disconnected'}")
    print(f"Degree statistics: Min= {stats['min_degree']}, Max={stats['max_degree']}, Avg={stats['avg_degree']:.2f}")

    visualize_graph(G, is_connected, degrees)

if __name__ == "__main__":
    main()

# This code is a basic example of how to use the graph_analysis package. It generates a random graph, analyzes its connectivity and vertex degrees, and visualizes the graph with degree information.