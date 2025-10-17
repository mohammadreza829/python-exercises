def my_gen(n):
    n=1
    while True:
        yield str(n)*n
        n+=1

g=my_gen(3)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


