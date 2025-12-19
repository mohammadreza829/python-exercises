a = [29, 10, 14, 37, 13, 25, 18]
for i in range(1, len(a)):
    item = a[i]
    j = i
    while j > 0 and a[j - 1] > item :
        a[j] = a[j - 1]
        j -= 1
        a[j] = item
    print(a)
print(a)


