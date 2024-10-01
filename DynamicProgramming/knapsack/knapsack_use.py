from inputControl import get_continue_choice, get_positive_int
from knapsack_rec import knapsack

# this file is to interactively test the knapsack solution, if you want to do a unittest, use test_knapsack.py instead
W = get_positive_int("Insert max weight (positive integer): ")  # Max weight of the knapsack
i = 0
M = []
Obj = []  # List to store (value, weight) of each object

# Collecting the items' weight and value
while True:
    w = get_positive_int(f"Insert weight of object {i} (positive integer): ")  # weight of the object
    v = get_positive_int(f"Insert value of object {i} (positive integer): ")   # value of the object
    Obj.append((v, w))  # Append as a tuple (value, weight)
    i += 1
    if get_continue_choice("Continue adding objects? (Y/n): ") == 'N':
        break

n = len(Obj)  # Number of items

# Initialize the matrix M with -1
# M will have dimensions (n+1) x (W+1), as we consider 0..n items and 0..W capacity
M = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

# Solve the knapsack problem
max_value = knapsack(n, W, M, Obj)

# Optional: Printing to verify initialization
print("Objects (value, weight):", Obj)
print("Matrix M:", M)
print(f"Maximum value that can be obtained: {max_value}")