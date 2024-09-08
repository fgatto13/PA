def Fib(n) -> int:
    memo = [-1] * (n+1)
    if n <= 1:
        return n
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[i-1]
    return memo[n]

print(Fib(int(input("insert a number: "))))
