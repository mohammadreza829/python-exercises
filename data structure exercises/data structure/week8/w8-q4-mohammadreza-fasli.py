def quick_sort_projects(items):
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]  
    less = []
    equal = []
    greater = []

    for x in items:
        if x[0] < pivot[0]:
            less.append(x)
        elif x[0] > pivot[0]:
            greater.append(x)
        else:
            equal.append(x)

    return quick_sort_projects(less) + equal + quick_sort_projects(greater)

if __name__ == "__main__":
    n = int(input().strip())
    projects = []

    for _ in range(n):
        line = input().rstrip()
        parts = line.split()
        complexity = int(parts[0])
        name = " ".join(parts[1:])
        projects.append((complexity, name))

    sorted_projects = quick_sort_projects(projects)

    for complexity, name in sorted_projects:
        print(f"{complexity} {name}")
