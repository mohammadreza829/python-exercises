s = input().strip()

def parse_point(token):
    xs, ys = token.strip().split()
    return float(xs), float(ys)

tokens = [t for t in s.split(',') if t.strip()]

points = [parse_point(t) for t in tokens]

valid_points = [
    (x, y)
    for x, y in points
    if x * x + y * y <= 16 and ((x > 0 and y > 0) or (x < 0 and y < 0))
]

print(len(valid_points))
