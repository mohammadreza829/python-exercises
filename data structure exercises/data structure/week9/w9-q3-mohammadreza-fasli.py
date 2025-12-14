line = input().strip()
if line == "":
    print()
else:
    ids = list(map(int, line.split()))


    ids.sort()
    print(" ".join(str(x) for x in ids))
