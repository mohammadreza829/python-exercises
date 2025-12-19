import sys

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i : i + 5] for i in range(0, len(arr), 5)]

    medians = [sorted(sub)[len(sub) // 2] for sub in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2)

    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        high = [x for x in arr if x > pivot]
        return median_of_medians(high, k - len(low) - len(equal))


def main():
    input_data = sys.stdin.read().splitlines()

    if len(input_data) >= 2:
        nums = list(map(int, input_data[0].split()))
        k = int(input_data[1])


        target_index = len(nums) - k

        result = median_of_medians(nums, target_index)
        print(result)


if __name__ == "__main__":
    main()
