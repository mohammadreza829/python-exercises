def solution():

    line = input().split()
    n = int(line[0])

    buckets = {}
    for i in range(1, len(line), 2):
        name = line[i]
        zip_code = line[i + 1]
        prefix = zip_code[:2]

        if prefix not in buckets:
            buckets[prefix] = 0
        buckets[prefix] += 1

    sorted_buckets = sorted(buckets.items(), key=lambda x: int(x[0]), reverse=True)

    for prefix, count in sorted_buckets:
        print(f"{prefix} {count}")

solution()
