A = [4, 2, 2, 8, 3, 3, 1]
m = max(A)
count = [0] * (m + 1)
## print(count)
for i in A:
    count[i] += 1

print(count)

A_sorted = []
for i in range(len(count)):
    A_sorted += [i] * count[i]

print(A_sorted)
