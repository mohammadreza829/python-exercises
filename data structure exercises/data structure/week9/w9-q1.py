def hash_name(name, size):
    s = 0
    for ch in name:
        s += ord(ch)
    return s % size


def main():
    parts = input().strip().split(",")
    names = [p.strip() for p in parts if p.strip()]

    size = 5
    table = [[] for _ in range(size)]

    def rehash():
        nonlocal size, table
        old = [name for bucket in table for name in bucket]
        size *= 2
        table = [[] for _ in range(size)]
        for name in old:
            idx = hash_name(name, size)
            table[idx].append(name)

    for name in names:
        count = sum(len(b) for b in table)
        if count >= size:
            rehash()
        idx = hash_name(name, size)
        table[idx].append(name)

    for i, bucket in enumerate(table):
        print(f"خانه {i}: {bucket}")


main()
