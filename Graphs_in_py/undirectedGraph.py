class UndirectedGraph:
    def __init__(self, n):
        # Initialize an empty adjacency list for n nodes
        self.graph = [[] for _ in range(n)]
        self.num_nodes = n

    def add_edge(self, u, v):
        # Add the edge in both directions
        if u < self.num_nodes and v < self.num_nodes:
            self.graph[u].append(v)
            self.graph[v].append(u)  # Add the reverse edge automatically
        else:
            print("Invalid nodes. Please enter valid node indices.")

    def display_graph(self):
        for node in range(self.num_nodes):
            print(f"Node {node}: {self.graph[node]}")

# Example usage:
undirected_graph = UndirectedGraph(5)  # Initialize a graph with 5 nodes
undirected_graph.add_edge(1, 2)  # Adds both (1, 2) and (2, 1)
undirected_graph.add_edge(0, 3)  # Adds both (0, 3) and (3, 0)
undirected_graph.display_graph()
