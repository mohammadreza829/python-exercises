n = int(input().strip())
m = int(input().strip())

adjacency = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjacency[u].append(v)

start, target = map(int, input().split())

stack = [start]
seen = [False] * n
seen[start] = True
ok = False

while stack:
    u = stack.pop()
    if u == target:
        ok = True
        break
    for v in adjacency[u]:
        if not seen[v]:
            seen[v] = True
            stack.append(v)

print("True" if ok else "False")
