a = list(map(int, input().split()))
start = 0
end = len(a) - 1

while start < end:
    min_idx = start
    max_idx = start
    for i in range(start, end + 1):
        if a[i] < a[min_idx]:
            min_idx = i
        if a[i] > a[max_idx]:
            max_idx = i
    a[start], a[min_idx] = a[min_idx], a[start]

    if max_idx == start:
        max_idx = min_idx
    a[end], a[max_idx] = a[max_idx], a[end]
    start += 1
    end -= 1

print(a)
