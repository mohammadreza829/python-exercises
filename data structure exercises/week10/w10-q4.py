from collections import deque
from itertools import combinations

n = int(input().strip())
m = int(input().strip())

edges = []
for _ in range(m):
    u, v, eid = map(int, input().split())
    edges.append((u, v, eid))

start, target = map(int, input().split())

def reachable(blocked_ids):
    blocked = set(blocked_ids)
    adj = [[] for _ in range(n)]
    for u, v, eid in edges:
        if eid not in blocked:
            adj[u].append(v)

    q = deque([start])
    seen = [False] * n
    seen[start] = True

    while q:
        u = q.popleft()
        if u == target:
            return True
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return False

answer = -1

for k in range(m + 1):
    found = False
    all_ids = [eid for _, _, eid in edges]
    for combo in combinations(all_ids, k):
        if not reachable(combo):
            answer = k
            found = True
            break
    if found:
        break

print(answer)
