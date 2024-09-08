def karatsuba(x, y):
    # Base case: single-digit multiplication
    if x < 10 or y < 10:
        return x * y
    
    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    # Split the digits
    x1 = x // 10**half
    x0 = x % 10**half
    y1 = y // 10**half
    y0 = y % 10**half
    
    # Recursively compute the products
    P1 = karatsuba(x1, y1)
    P2 = karatsuba(x0, y0)
    P3 = karatsuba(x1 + x0, y1 + y0)
    
    # Combine the results using the Karatsuba formula
    return P1 * 10**(2*half) + (P3 - P1 - P2) * 10**half + P2
