def quick_select_kth_largest(arr, k):

    if not (1 <= k <= len(arr)):
        raise ValueError("k is out of range")

    def select(lst, k_pos):
        if len(lst) == 1:
            return lst[0]

        pivot = lst[0]
        greater = [x for x in lst[1:] if x > pivot]
        equal   = [x for x in lst if x == pivot]
        smaller = [x for x in lst[1:] if x < pivot]

        if k_pos <= len(greater):
            return select(greater, k_pos)
        elif k_pos <= len(greater) + len(equal):
            return pivot
        else:
            new_k = k_pos - (len(greater) + len(equal))
            return select(smaller, new_k)

    return select(arr, k)

if __name__ == "__main__":
    n = int(input().strip())
    waits = list(map(int, input().split()))
    k = int(input().strip())

    ans = quick_select_kth_largest(waits, k)
    print(ans)
