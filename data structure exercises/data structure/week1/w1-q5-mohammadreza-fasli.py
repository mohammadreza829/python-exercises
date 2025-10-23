A = input().split()


def radix_sort(A):
    max_len = max(len(num) for num in A)
    for exp in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(10)]
        for num in A:

            digit = int(num[exp]) if exp < len(num) else 0

            digit = int(num.zfill(max_len)[exp])
            buckets[digit].append(num)
        A = []
        for bucket in buckets:
            A.extend(bucket)
    return A


result = radix_sort(A)
print(result)
