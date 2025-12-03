import random


def randomized_quick_sort(items):
    if len(items) <= 1:
        return items

    pivot = random.choice(items)
    bigger, equal, smaller = [], [], []

    for e in items:
        if e[0] > pivot[0]:
            bigger.append(e)
        elif e[0] < pivot[0]:
            smaller.append(e)
        else:
            equal.append(e)

    return randomized_quick_sort(bigger) + equal + randomized_quick_sort(smaller)


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for _ in range(n):
        line = input().rstrip()
        parts = line.split()
        num = int(parts[0])
        name = " ".join(parts[1:])
        arr.append((num, name))

    sorted_arr = randomized_quick_sort(arr)

    for num, name in sorted_arr:
        print(f"{name} , {num}")
