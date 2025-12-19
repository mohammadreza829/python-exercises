INF = 10**18

def bellman_ford(n, edges, s):
    d = [INF] * n
    d[s] = 0
    for _ in range(n - 1):
        any_update = False
        for u, v, w in edges:
            if d[u] != INF and d[u] + w < d[v]:
                d[v] = d[u] + w
                any_update = True
        if not any_update:
            break
    return d

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

distances = bellman_ford(n, edges, s)
print(-1 if distances[t] == INF else distances[t])
