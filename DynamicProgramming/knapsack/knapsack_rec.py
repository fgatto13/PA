# knapsack_rec.py
def knapsack(i, w, M, Obj):
    if i == 0 or w == 0:
        M[i][w] = 0  # Base case: no items or zero capacity
        return 0
    if M[i][w] != -1:
        return M[i][w]  # If value is already computed, return it

    value_i = Obj[i-1][0]  # The value of the i-th item (Obj is 0-indexed)
    weight_i = Obj[i-1][1]  # The weight of the i-th item

    if weight_i > w:
        # Item cannot be included because it's too heavy, skip it
        M[i][w] = knapsack(i-1, w, M, Obj)
    else:
        # Choose the maximum between including and not including the item
        M[i][w] = max(knapsack(i-1, w, M, Obj),  # Exclude the item
                      knapsack(i-1, w-weight_i, M, Obj) + value_i)  # Include the item

    return M[i][w]

# Helper function to initialize the problem
def initialize_knapsack(W, Obj):
    n = len(Obj)  # Number of items
    M = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]  # Initialize matrix
    return knapsack(n, W, M, Obj)  # Call the knapsack function and return the result
