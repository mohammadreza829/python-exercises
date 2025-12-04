TABLE_SIZE = 1009

def make_table(m=TABLE_SIZE):
    return [[] for _ in range(m)]

def h(key, m):
    return key % m

def ht_insert(table, sid, name, gpa):
    idx = h(sid, len(table))
    bucket = table[idx]
    for i, (k, _, _) in enumerate(bucket):
        if k == sid:
            bucket[i] = (sid, name, gpa)
            return
    bucket.append((sid, name, gpa))

def ht_search(table, sid):
    idx = h(sid, len(table))
    for k, name, gpa in table[idx]:
        if k == sid:
            return f"{name},{gpa}"
    return "None"

def ht_delete(table, sid):
    idx = h(sid, len(table))
    bucket = table[idx]
    for i, (k, _, _) in enumerate(bucket):
        if k == sid:
            bucket.pop(i)
            return

if __name__ == "__main__":
    q = int(input().strip())
    ht = make_table()

    for _ in range(q):
        parts = input().split()
        cmd = parts[0]

        if cmd == "insert":
            sid = int(parts[1])
            name = parts[2]
            gpa = float(parts[3])
            ht_insert(ht, sid, name, gpa)
        elif cmd == "search":
            sid = int(parts[1])
            print(ht_search(ht, sid))
        elif cmd == "delete":
            sid = int(parts[1])
            ht_delete(ht, sid)
