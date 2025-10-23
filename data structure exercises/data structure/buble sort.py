A = [5, 1, 4, 2, 8]
n = len(A)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
    print(f'دور {i+1}:', A)
print('مرتب نهایی:', A)
print(n)