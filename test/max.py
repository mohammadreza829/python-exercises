def func(*a):
    y=a[0]
    for i in a:
        if i>=y :
            y = i
    return y

print("max:",func(68,54,4845,264))