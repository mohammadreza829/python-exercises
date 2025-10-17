def func(*a):
    y=0
    for i in a:
        y += 1
    return y

s= ("1","2","3")

print(func(*s))