def partition(arr, low, high):
    pivot = arr[high][0]   
    i = low - 1
    for j in range(low, high):
        if arr[j][0] >= pivot:   
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p + 1, high)


if __name__ == "__main__":
    n = int(input().strip())
    events = []
    for _ in range(n):
        line = input().rstrip()
        parts = line.split()
        cnt = int(parts[0])
        name = " ".join(parts[1:])
        events.append((cnt, name))

    quick_sort_inplace(events, 0, len(events) - 1)

    for cnt, name in events:
        print(f"{name} , {cnt}")
