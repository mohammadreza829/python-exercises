def parse_event(line):
    line = line.rstrip().replace("",",").replace("،", ",")
    tokens = line.split()
    if "," not in line and tokens and tokens[0].isdigit():
        att = int(tokens[0])
        title = " ".join(tokens[1:])
    else:
        name_part, num_part = line.split(",", 1)
        title = name_part.strip()
        att = int(num_part.strip())
    return title, att


def partition(arr, lo, hi):
    pivot_val = arr[hi][1]   
    i = lo - 1
    for j in range(lo, hi):
        if arr[j][1] >= pivot_val:    
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort_inplace(arr, lo, p - 1)
        quick_sort_inplace(arr, p + 1, hi)


if __name__ == "__main__":
    n = int(input().strip())
    events = []
    for _ in range(n):
        title, att = parse_event(input())
        events.append((title, att))

    quick_sort_inplace(events, 0, len(events) - 1)

    for title, att in events:
        print(f"{title}, {att}")
