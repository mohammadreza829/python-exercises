line = input().strip()

if line == "":
    print()
else:
    arr = list(map(int, line.split()))

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(" ".join(str(x) for x in arr))
