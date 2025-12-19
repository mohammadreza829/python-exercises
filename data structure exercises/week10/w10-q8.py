import heapq

INF = 10**18

n = int(input().strip())
m = int(input().strip())

adj = [[] for _ in range(n)]
neg = False

for _ in range(m):
    u, v, w = map(int, input().split())
    if w < 0:
        neg = True
    adj[u].append((v, w))
    adj[v].append((u, w))

energy_limit = int(input().strip())
start = int(input().strip())
k = int(input().strip())
stones = list(map(int, input().split())) if k > 0 else []

if neg:
    print(-1)
else:
    def shortest(src, dst):
        dist = [INF] * n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if u == dst:
                return d
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return INF

    time_sum = 0
    cur = start

    for x in stones:
        d = shortest(cur, x)
        if d == INF:
            print(-1)
            break
        time_sum += d
        cur = x
    else:
        d = shortest(cur, start)
        if d == INF:
            print(-1)
        else:
            time_sum += d
            print(time_sum)
