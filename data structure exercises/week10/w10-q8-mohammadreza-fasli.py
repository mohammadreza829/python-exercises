import heapq
import sys

INF = 10**18

data = sys.stdin.read().strip().split()
it = iter(data)

n = int(next(it))      
m = int(next(it))       

adj = [[] for _ in range(n)]

negative_edge = False

for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    w = int(next(it))
    if w < 0:
        negative_edge = True
    adj[u].append((v, w))
    adj[v].append((u, w))

energy_limit = int(next(it))   
start = int(next(it))
k = int(next(it))

stones = []
for _ in range(k):
    stones.append(int(next(it)))

if negative_edge:
    print(-1)
    sys.exit(0)

def dijkstra(src):
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

total_time = 0
current = start

for target in stones:
    dist = dijkstra(current)
    if dist[target] == INF:
        print(-1)
        sys.exit(0)
    total_time += dist[target]
    current = target

dist_back = dijkstra(current)
if dist_back[start] == INF:
    print(-1)
else:
    total_time += dist_back[start]
    print(total_time)
