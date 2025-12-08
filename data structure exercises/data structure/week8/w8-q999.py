TABLE_SIZE = 1009

class Node:
    def __init__(self, sid, name, gpa, nxt=None):
        self.sid = sid
        self.name = name
        self.gpa = gpa
        self.next = nxt

class StudentTable:
    def __init__(self, m=TABLE_SIZE):
        self.m = m
        self.table = [None] * m

    def _hash(self, sid):
        return sid % self.m

    def insert(self, sid, name, gpa):
        idx = self._hash(sid)
        head = self.table[idx]

        cur = head
        while cur:
            if cur.sid == sid:
                cur.name = name
                cur.gpa = gpa
                return
            cur = cur.next

        new_node = Node(sid, name, gpa, head)
        self.table[idx] = new_node

    def search(self, sid):
        idx = self._hash(sid)
        cur = self.table[idx]
        while cur:
            if cur.sid == sid:
                return f"{cur.name},{cur.gpa}"
            cur = cur.next
        return "None"

    def delete(self, sid):
        idx = self._hash(sid)
        cur = self.table[idx]
        prev = None
        while cur:
            if cur.sid == sid:
                if prev:
                    prev.next = cur.next
                else:
                    self.table[idx] = cur.next
                return
            prev, cur = cur, cur.next

if __name__ == "__main__":
    q = int(input().strip())
    ht = StudentTable()
    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "insert":
            sid = int(parts[1])
            name = parts[2]
            gpa = float(parts[3])
            ht.insert(sid, name, gpa)
        elif op == "search":
            sid = int(parts[1])
            print(ht.search(sid))
        elif op == "delete":
            sid = int(parts[1])
            ht.delete(sid)
