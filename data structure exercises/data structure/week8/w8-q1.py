def exists_with_binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while True:
        if lo > hi:
            return False
        mid = (lo + hi) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

if __name__ == "__main__":
    numbers_line = input().strip()
    arr = list(map(int, numbers_line.split())) if numbers_line else []

    t = int(input().strip())

    print(exists_with_binary_search(arr, t))
