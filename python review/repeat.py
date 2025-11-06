def rep(x , digit):
    # x = int(x)
    # digit = int(digit)
    w = 0
    for i in digit:
        if i == x :
            w += 1
    return w

x = input("enter a number : ")
digit = input("enter a number : ")
print(rep(x , digit))