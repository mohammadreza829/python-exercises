points_str = input().strip()

parts = points_str.split(',')

count = 0

for part in parts:
    part = part.strip()
    if not part:
        continue

    x_str, y_str = part.split()
    x = float(x_str)
    y = float(y_str)

    if x * x + y * y <= 16:

        if (x > 0 and y > 0) or (x < 0 and y < 0):
            count += 1

print(int(count))
