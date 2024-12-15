def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def convex_hull(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))
    n = len(points)

    if n < 3:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != -1:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != -1:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

points = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 3), (3, 0), (1, 2), (2, 1)]
hull = convex_hull(points)
print("Convex Hull:", hull)




