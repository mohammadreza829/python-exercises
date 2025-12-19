INF = 10**18

n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

s, t = map(int, input().split())

dist = [INF] * n
dist[s] = 0

for _ in range(n - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        break

if dist[t] == INF:
    print(-1)
else:
    print(dist[t])
