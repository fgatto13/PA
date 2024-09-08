def Fib(n):
    if n <= 1:
        return n
    return Fib(n-2) + Fib(n-1)

print(Fib(int(input("inserire numero: "))))