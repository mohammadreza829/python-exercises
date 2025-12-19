def quick_sort(events):
    if len(events) <= 1:
        return events

    pivot = events[0]
    bigger = []
    smaller_equal = []

    for e in events[1:]:
        if e[1] > pivot[1]:
            bigger.append(e)
        else:
            smaller_equal.append(e)

    return quick_sort(bigger) + [pivot] + quick_sort(smaller_equal)

if __name__ == "__main__":
    n_line = input().strip()
    n = int(n_line)

    events = []
    for _ in range(n):
        line = input().rstrip()
        line = line.replace("،", ",")


        parts = line.split()
        if "," not in line and parts[0].isdigit():
            attendance = int(parts[0])
            name = " ".join(parts[1:])
        else:
            name_part, num_part = line.split(",", 1)
            name = name_part.strip()
            attendance = int(num_part.strip())

        events.append((name, attendance))

    sorted_events = quick_sort(events)

    for name, attendance in sorted_events:
        print(f"{name}, {attendance}")
