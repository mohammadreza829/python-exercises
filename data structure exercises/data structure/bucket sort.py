A = [29, 25, 9, 49, 3, 37, 21, 43]
max_num = max(A)


def get_bucket(x):

    return x // 1


bucket_num = get_bucket(max_num) + 1

buckets = [[] for i in range(bucket_num)]
print(buckets)
for i in A:

    buckets[get_bucket(i)] += [i]
    print(buckets)
print(buckets)
