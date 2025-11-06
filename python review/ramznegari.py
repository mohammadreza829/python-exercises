def ramz(x):
    for i in x:
        z = ord(i)
        y = z*2-3
        print(chr(y), end="")
def ramgoshaie(x):
    for i in x:
        z = ord(i)
        y = (z+3)//2
        print(chr(y), end="")

x = input("enter your chr: ")
print(ramz(x))

print(ramgoshaie(x))
        
