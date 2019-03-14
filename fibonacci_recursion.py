def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

n=8
for i in range(n):
    print(fib(i))

#output would be -> 0 1 1 2 3 5 8 13 21 34
