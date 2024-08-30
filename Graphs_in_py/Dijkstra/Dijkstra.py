from MinPriorityQueue import MinPriorityQueue
from weightedGraph import WeightedGraph

def create_graph() -> WeightedGraph:
    G = WeightedGraph(6)
    # Example edges with weights for debugging purposes
    G.add_edge(0, 1, 3)
    G.add_edge(1, 2, 2)
    G.add_edge(2, 3, 4)
    G.add_edge(3, 4, 1)
    G.add_edge(4, 5, 5)
    # For the graph to be connected, you might need more edges:
    G.add_edge(5, 0, 7)  # Just an example; modify as needed.
    return G

def dijkstra(G: WeightedGraph, s: int) -> dict:
    """
    Implement Dijkstra's algorithm for finding the shortest path from source node s to all other nodes in graph G.

    :param G: The weighted graph.
    :param s: The source node index.
    :return: A dictionary d where d[v] is the shortest distance from s to v.
    """
    n = G.n
    S = set()  # Explored nodes
    Q = MinPriorityQueue()  # Priority queue for unexplored nodes
    d = {u: float('inf') for u in range(n)}  # Distance dictionary initialized to infinity
    d[s] = 0

    # Initialize priority queue with all nodes
    Q.insert(0, s)  # Distance to source is 0
    for u in range(n):
        if u != s:
            Q.insert(float('inf'), u)

    print("Initial distances:", d)
    print("Initial queue:", Q.heap)

    while not Q.is_empty():
        dist_u, u = Q.extract_min()  # Get the node with the smallest distance
        print(f"Extracted node {u} with distance {dist_u}")
        S.add(u)

        for v, length in G.graph[u]:  # For all adjacent nodes (v, length)
            if v not in S:  # Only consider unvisited nodes
                new_dist = d[u] + length
                if new_dist < d[v]:  # Found a shorter path to v
                    print(f"Updating distance of node {v} from {d[v]} to {new_dist}")
                    d[v] = new_dist
                    Q.decrease_key(v, new_dist)
                    print("content of the queue: ", d, "\n")

    print("Final distances:", d)
    return d

# Example usage
G = create_graph()
print("Graph structure:")
G.display_graph()  # Debugging print of graph structure

s = int(input("Enter the source node: "))
if 0 <= s < G.n:  # Check if source node is valid
    distances = dijkstra(G, s)
    print("Shortest distances from node", s, ":", distances)
else:
    print(f"Invalid source node. Please enter a value between 0 and {G.n - 1}.")
