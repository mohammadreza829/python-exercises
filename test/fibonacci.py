#0,1,1,2,3,5,8,13,21,...
def my_gen(x):
    a,b=0,1
    for _ in range(x):
        yield a
        a,b=b,a+b

g=my_gen(20)
for q in g:
    print(q)

