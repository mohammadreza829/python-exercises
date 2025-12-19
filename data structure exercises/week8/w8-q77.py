def accepted_count(desc_list, threshold):
    lo, hi = 0, len(desc_list) - 1
    last_valid = -1

    while True:
        if lo > hi:
            break
        mid = (lo + hi) // 2
        if desc_list[mid] >= threshold:
            last_valid = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return last_valid + 1

if __name__ == "__main__":
    line = input().strip()
    data = list(map(int, line.split())) if line else []
    k = int(input().strip())

    print(accepted_count(data, k))
