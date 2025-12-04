TABLE_SIZE = 1009  

class HashTable:
    def __init__(self, size=TABLE_SIZE):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, sid, name, gpa):
        idx = self._hash(sid)
        bucket = self.buckets[idx]

        for i, (st_id, _, _) in enumerate(bucket):
            if st_id == sid:
                bucket[i] = (sid, name, gpa)
                return

        bucket.append((sid, name, gpa))

    def search(self, sid):
        idx = self._hash(sid)
        for st_id, name, gpa in self.buckets[idx]:
            if st_id == sid:
                return f"{name},{gpa}"
        return "None"

    def delete(self, sid):
        idx = self._hash(sid)
        bucket = self.buckets[idx]
        for i, (st_id, _, _) in enumerate(bucket):
            if st_id == sid:
                bucket.pop(i)
                return
if __name__ == "__main__":
    n = int(input().strip())
    table = HashTable()

    for _ in range(n):
        parts = input().split()
        cmd = parts[0]

        if cmd == "insert":
            sid = int(parts[1])
            name = parts[2]
            gpa = float(parts[3])
            table.insert(sid, name, gpa)

        elif cmd == "search":
            sid = int(parts[1])
            print(table.search(sid))

        elif cmd == "delete":
            sid = int(parts[1])
            table.delete(sid)
