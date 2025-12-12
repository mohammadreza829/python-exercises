def hash_name(name, size):
    total = 0
    for ch in name:
        total += ord(ch)
    return total % size

line = input().strip()
names = [x.strip() for x in line.split(",") if x.strip()]

size = 5
table = [[] for _ in range(size)]

def rehash_all():
    global size, table
    old_items = []
    for bucket in table:
        for name in bucket:
            old_items.append(name)
    size *= 2
    table = [[] for _ in range(size)]
    for name in old_items:
        idx = hash_name(name, size)
        table[idx].append(name)

for name in names:

    current_count = sum(len(b) for b in table)
    if current_count >= size:
        rehash_all()

    index = hash_name(name, size)
    table[index].append(name)

for i, bucket in enumerate(table):
    print(f"خانه{i}: {bucket}")
