def fib(x):
    a,b = 0,1
    for i in range(0,x+1):
        print(a)
        a,b = b,a+b
print(fib(10))