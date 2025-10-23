def two_way_bubble_sort(arr):
    n = len(arr)
    if n == 0:
        return arr, 0, 0
    left = 0
    right = n - 1
    comparisons = 0
    swaps = 0
    swapped = True
    while swapped and left < right:
        swapped = False
        for i in range(left, right):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        right -= 1
        if not swapped:
            break
        for i in range(right, left, -1):
            comparisons += 1
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
                swapped = True
        left += 1
    return arr, comparisons, swaps
arr = list(map(float, input().split()))
result, comps, swaps = two_way_bubble_sort(arr)
print(result)
print(comps)
print(swaps)



 

