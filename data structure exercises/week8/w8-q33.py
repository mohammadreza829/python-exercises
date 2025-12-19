import random

def normalize_line(line):
    line = line.strip().replace("،", ",")
    parts = line.split()
    if "," not in line and parts and parts[0].isdigit():
        att = int(parts[0])
        name = " ".join(parts[1:])
    else:
        left, right = line.split(",", 1)
        name = left.strip()
        att = int(right.strip())
    return name, att


def randomized_quick_sort(events):
    if len(events) <= 1:
        return events

    pivot = random.choice(events)
    greater, equal, less = [], [], []

    for ev in events:
        if ev[1] > pivot[1]:
            greater.append(ev)
        elif ev[1] < pivot[1]:
            less.append(ev)
        else:
            equal.append(ev)

    return randomized_quick_sort(greater) + equal + randomized_quick_sort(less)


if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for _ in range(n):
        nm, at = normalize_line(input())
        arr.append((nm, at))

    sorted_arr = randomized_quick_sort(arr)
    for nm, at in sorted_arr:
        print(f"{nm}, {at}")
