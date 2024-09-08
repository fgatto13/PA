# this version of the Fibonacci algorithm 
# uses memoization to solve the problem in O(n)
# memoization equals to top-down programming, 
# using a global/local variable 
# to keep track of the solutions 
# of the overlapping sub-problems

def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(int(input("insert number: "))))