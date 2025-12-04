def quick_sort_projects(items):
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    less = []
    equal = []
    greater = []

    for x in items:
        if x[1] < pivot[1]:      
            less.append(x)
        elif x[1] > pivot[1]:
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
        score = int(parts[0])
        name = " ".join(parts[1:])
        projects.append((name, score))

    
    sorted_projects = quick_sort_projects(projects)

    for name, score in sorted_projects:
        print(f"{name} , {score}")
