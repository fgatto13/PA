class WeightedGraph:
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

    def add_edge(self, u, v, l):
        """
        Add a directed edge from node u to node v with a value l.
        
        :param u: Source node index.
        :param v: Destination node index.
        :param l: Value (e.g., weight, length, or cost) associated with the edge.
        """
        if 0 <= u < self.n and 0 <= v < self.n:  # Check if u and v are valid nodes
            self.graph[u].append((v, l))  # Store the edge as a tuple (v, l)
        else:
            raise ValueError("Invalid edge. One or both nodes are out of bounds.")

    def get_edge_value(self, u, v):
        """
        Get the value of the edge from node u to node v.
        
        :param u: Source node index.
        :param v: Destination node index.
        :return: Value (e.g., weight, length, or cost) of the edge (u, v), or None if the edge does not exist.
        """
        if 0 <= u < self.n:
            for (dest, l) in self.graph[u]:
                if dest == v:
                    return l
            return None  # Edge not found
        else:
            raise ValueError("Invalid node index. Node index should be between 0 and " + str(self.n - 1))

    def display_graph(self):
        """
        Display the adjacency list representation of the graph with edge values.
        """
        for i in range(self.n):
            edges = ", ".join([f"({v}, {l})" for v, l in self.graph[i]])
            print(f"Node {i}: {edges}")