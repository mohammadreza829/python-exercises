

A= list(map(int, input().split()))
n = len(A)
is_sorted = False
while is_sorted == False:
    is_sorted = True
    for i in range(n - 1, 0, -2):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            is_sorted = False
    for i in range(n - 2, 0, -2):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            is_sorted = False
print(A)


