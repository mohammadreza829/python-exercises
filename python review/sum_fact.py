def sum_fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x
print(sum_fact(5))

