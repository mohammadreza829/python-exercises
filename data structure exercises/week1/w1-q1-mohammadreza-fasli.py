a = list(map(int, input().split()))
m = max(a)
offset = abs(min(a))
count = [0] * (m + offset + 1)
a_sorted = []
for i in a:
    count[i + offset] += 1
for i in range(len(count)):
    a_sorted += [i - offset] * count[i]
print(a_sorted)

