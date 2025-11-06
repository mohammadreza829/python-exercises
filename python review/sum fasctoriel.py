def fact(x):
    p = 0
    for i in range(0,x+1):
        p += i
    return p
        
x = int(input("enter your number : "))
print(fact(x))
