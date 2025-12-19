def insertion(a):
    for i in range(1, len(a)):
        item = a[i]
        j = i
        while j > 0 and a[j - 1] > item:
            a[j] = a[j - 1]
            j -= 1
        a[j] = item
    return a

A = list(map(int, input().split()))

# تعداد سطل‌ها باید بر اساس بیشترین رقم عدد تنظیم بشه!
max_digits = max(len(str(x)) for x in A)
buckets_count = 10 ** (max_digits - 1)
buk = [[] for _ in range(buckets_count)]
for num in A:
    index = num // buckets_count
    buk[index].append(num)

for i in range(len(buk)):
    buk[i] = insertion(buk[i])

bukets = []
for j in buk:
    bukets += j

# همه داده‌ها را به سه رقمی با صفر جلو تبدیل کن (اگر عدد چهار رقمی بود همان را نگه دار)
final = [f"{x:03d}" for x in bukets]
print('[' + ', '.join(final) + ']')

