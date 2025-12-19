from collections import deque
from itertools import combinations

n = int(input().strip())
m = int(input().strip())

edges = []
for _ in range(m):
    u, v, eid = map(int, input().split())
    edges.append((u, v, eid))

start, target = map(int, input().split())

def has_path(removed_ids):
    adj = [[] for _ in range(n)]
    removed_set = set(removed_ids)
    for u, v, eid in edges:
        if eid not in removed_set:
            adj[u].append(v)

    q = deque([start])
    visited = [False] * n
    visited[start] = True

    while q:
        u = q.popleft()
        if u == target:
            return True
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return False

answer = -1

for k in range(m + 1):
    found_cut = False
    for combo in combinations(range(m), k):
        removed_eids = [edges[i][2] for i in combo]
        if not has_path(removed_eids):
            answer = k
            found_cut = True
            break
    if found_cut:
        break

print(answer)
