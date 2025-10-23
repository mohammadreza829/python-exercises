arr = list(map(float, input().replace(",", " ").split()))
num_len = len(arr)
arr2 = arr.copy()
for i in range(1):
    swapped = False
    for j in range(num_len - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if arr == sorted(arr2):
        print("YES")
    else:
        print("NO")
