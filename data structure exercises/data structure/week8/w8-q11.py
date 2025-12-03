import bisect

if __name__ == "__main__":
    line = input().strip()
    data = list(map(int, line.split())) if line else []

    target = int(input().strip())

    idx = bisect.bisect_left(data, target)

    exists = (idx < len(data) and data[idx] == target)
    print(exists)
