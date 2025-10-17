def func1(a):
    y=[]
    for i in range(1,a+1):
        if a%i==0:
            y.append(i)
    return y

def func2(z):
    p= func1(z)
    for i in (p):
        if z%i==0 and i*i==z:
            return("yes")
    else:
        return("no")

print(func2(16))