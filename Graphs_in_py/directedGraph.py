class DirectedGraph:
    def __init__(self, n):
        """
        Initialize a directed graph with n nodes.
        
        :param n: Number of nodes in the graph.
        """
        self.n = n  # Number of nodes
        self.graph = [[] for _ in range(n)]  # Initialize adjacency lists for each node

    def add_node(self):
        """
        Add a new node to the graph by expanding the adjacency list.
        """
        self.graph.append([])
        self.n += 1

    def add_edge(self, u, v):
        """
        Add a directed edge from node u to node v.
        
        :param u: Source node index.
        :param v: Destination node index.
        """
        if 0 <= u < self.n and 0 <= v < self.n:  # Check if u and v are valid nodes
            self.graph[u].append(v)
        else:
            raise ValueError("Invalid edge. One or both nodes are out of bounds.")

    def display_graph(self):
        """
        Display the adjacency list representation of the graph.
        """
        for i in range(self.n):
            print(f"Node {i}: {self.graph[i]}")

# Example usage within another script or class:
# Initialize a graph with 3 nodes
g = DirectedGraph(3)

# Add edges programmatically
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

# Display the graph
g.display_graph()

# Adding a new node and an edge to it
g.add_node()
g.add_edge(3, 1)
g.display_graph()
