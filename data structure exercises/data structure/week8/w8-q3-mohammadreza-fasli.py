def quick_sort_events(events):

    if len(events) <= 1:
        return events

    pivot = events[0] 
    less = []
    greater = []

    for item in events[1:]:

        if item[0] > pivot[0]:
            greater.append(item)
        else:
            less.append(item)


    return quick_sort_events(greater) + [pivot] + quick_sort_events(less)

if __name__ == "__main__":
    n = int(input().strip())
    events = []

    for _ in range(n):
        line = input().rstrip()

        parts = line.split()
        attendance = int(parts[0])
        name = " ".join(parts[1:])
        events.append((attendance, name))

    sorted_events = quick_sort_events(events)

    for attendance, name in sorted_events:
        print(f"{name} , {attendance}")
