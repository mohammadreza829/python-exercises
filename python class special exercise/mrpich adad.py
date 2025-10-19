

x = [
    [25, 24, 23, 22, 21],
    [10, 9, 8, 7, 20],
    [11, 2, 1, 6, 19],
    [12, 3, 4, 5, 18],
    [13, 14, 15, 16, 17],
]


a = list(map(lambda row: print(" ".join(f"{num:2}" for num in row)), x))
print(a)

