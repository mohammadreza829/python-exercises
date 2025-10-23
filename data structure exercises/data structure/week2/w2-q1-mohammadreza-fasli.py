def two_way_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    comparisons = 0
    swaps = 0
    while left < right:

        for i in range(left, right):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        right -= 1
        for i in range(right, left, -1):
            comparisons += 1
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
        left += 1
    return arr, comparisons, swaps

arr = list(map(float, input().split()))
result, comps, swaps = two_way_bubble_sort(arr)
print(result)
print(comps)
print(swaps)



































































































