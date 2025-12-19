def insertion(a):
    for i in range(1, len(a)):
        item = a[i]
        j = i
        while j > 0 and a[j - 1] > item:
            a[j] = a[j - 1]
            j -= 1
        a[j] = item
    return a


A = list(map(float, input().split()))
minimum = min(A)
maximum = max(A)
n = len(A)
bucket_count = int(maximum) - int(minimum) + 1

buckets = [[] for _ in range(bucket_count)]

for num in A:
    index = int(num - minimum)
    buckets[index].append(num)

for i in range(len(buckets)):
    buckets[i] = insertion(buckets[i])

result = []
for b in buckets:
    result += b

print(result)
