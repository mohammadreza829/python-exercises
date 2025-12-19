import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))      
m = int(next(it))      

adj = [[] for _ in range(n)]
for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    adj[u].append(v)  

start = int(next(it))
target = int(next(it))

from collections import deque

visited = [False] * n
q = deque([start])
visited[start] = True
found = False

while q:
    u = q.popleft()
    if u == target:
        found = True
        break
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

print("True" if found else "False")
