def fib(n):
    lst = [0,1]
    for i in range(0,n):
        lst.append(lst[i] + lst[i+1])
    print(lst)

fib(8)
#output should be -> 0 1 1 2 3 5 8 13 21 34
