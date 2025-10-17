from random import random , randint
a = []
b = []
for i in range(10):
    for j in range(10):
        a.append(randint(0,1))
    b.append(a)
    a = []
for i in range(10):
    for j in range(10):
        print(b[i][j], end=' ')
    print()


