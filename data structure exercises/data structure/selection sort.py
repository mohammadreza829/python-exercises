def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print(a)
    return a

a = [29, 10, 14, 37, 13, 25, 18]
print(selection_sort(a))
