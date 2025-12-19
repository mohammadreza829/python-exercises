def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comparisons = 0
    swaps = 0
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                comparisons += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
        gap //= 2
    
    return arr, comparisons, swaps

arr = list(map(float, input().split()))
result, comps, swaps = shell_sort(arr)
print(result)
print(comps)
print(swaps)

