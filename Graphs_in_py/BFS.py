# Initialize the adjacency list for the graph
graph = []  # List of lists to represent the graph

# Get the number of nodes
print("Insert the number of nodes:")
n = int(input())  # Number of nodes

# Initialize the graph with empty adjacency lists for each node
for i in range(n):
    graph.append([])

# Populate the adjacency lists
for i in range(n):
    print(f"Adding edges for node {i}:")
    
    while True:
        print("Insert adjacent node index (or -1 to stop):")
        adjacent_node = int(input())
        
        if adjacent_node == -1:
            break
        
        # Ensure the node exists in the range of nodes
        if 0 <= adjacent_node < n:
            graph[i].append(adjacent_node)
        else:
            print(f"Invalid node index {adjacent_node}. Please enter a value between 0 and {n - 1}.")

# Print the adjacency list representation of the graph
print("\nGraph adjacency list:")
for i in range(n):
    print(f"Node {i}: {graph[i]}")

print("insert source node:")
start_node = int(input())
# Initialize levels list with empty lists
levels = []
levels.append([start_node])  # Start level 0 with the source node

visited = [False] * len(graph)  # Keep track of visited nodes
visited[start_node] = True

# Loop through each level
i = 0
while i < len(levels) and levels[i]:
    current_level = levels[i]
    next_level = []

    for u in current_level:
        for v in graph[u]:
            if not visited[v]:
                next_level.append(v)
                visited[v] = True

    if next_level:
        levels.append(next_level)
    i += 1

    # Output the levels
print("Levels:", levels)