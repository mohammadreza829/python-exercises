line = input().split()
n = int(line[0])

buckets = {}

i = 1
while i < len(line):
    name = line[i]
    zip_code = line[i + 1]
    prefix = zip_code[:2]

    if prefix in buckets:
        buckets[prefix] += 1
    else:
        buckets[prefix] = 1

    i += 2

sorted_items = sorted(buckets.items(), key=lambda x: int(x[0]), reverse=True)

for key, count in sorted_items:
    print(key, count)
