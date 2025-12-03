def quick_select_kth_largest(arr, k):
    def select(lst, kk):
        if len(lst) == 1:
            return lst[0]

        pivot = lst[0]
        greater = [x for x in lst[1:] if x > pivot]
        equal   = [x for x in lst if x == pivot]
        smaller = [x for x in lst[1:] if x < pivot]

        if kk <= len(greater):
            return select(greater, kk)
        elif kk <= len(greater) + len(equal):
            return pivot
        else:
            return select(smaller, kk - len(greater) - len(equal))

    return select(arr, k)

if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().split()))
    k = int(input().strip())
    print(quick_select_kth_largest(nums, k))
