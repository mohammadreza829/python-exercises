import sys


def median_of_three(arr, low, high):
    mid = (low + high) // 2

    a = arr[low][0]
    b = arr[mid][0]
    c = arr[high][0]

    if (a - b) * (c - a) >= 0:
        return low
    elif (a - b) * (c - b) >= 0:
        return mid
    else:
        return high


def partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high][0]  

    i = low - 1
    for j in range(low, high):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)


        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def main():

    input_data = sys.stdin.read().splitlines()

    if not input_data:
        return

    try:
        n = int(input_data[0].strip())
        projects = []

        for line in input_data[1:]:
            if not line.strip():
                continue

            parts = line.split(",")
            score = int(parts[0].strip())
            name = parts[1].strip()
            projects.append((score, name))

        quick_sort(projects, 0, len(projects) - 1)

        for p in projects:
            print(f"{p[0]} , {p[1]}")

    except ValueError:
        print("فرمت ورودی صحیح نیست.")


if __name__ == "__main__":
    main()
