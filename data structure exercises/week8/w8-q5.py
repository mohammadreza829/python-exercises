def quick_select_kth_smallest(arr, k):
    def select(lst, kk):
        if len(lst) == 1:
            return lst[0]

        pivot = lst[0]
        less   = [x for x in lst[1:] if x < pivot]
        equal  = [x for x in lst if x == pivot]
        greater= [x for x in lst[1:] if x > pivot]

        if kk <= len(less):
            return select(less, kk)
        elif kk <= len(less) + len(equal):
            return pivot
        else:
            return select(greater, kk - len(less) + -len(equal))

    return select(arr, k)


def kth_largest_via_smallest(arr, k):
    n = len(arr)
    return quick_select_kth_smallest(arr, n - k + 1)


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().split()))
    k = int(input().strip())
    print(kth_largest_via_smallest(nums, k))
