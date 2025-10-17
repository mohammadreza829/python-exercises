def sum2(*a):
    y=0
    for i in a:
       y +=i
       i +=1
    return y

print(sum2(1,2,3,4,5))