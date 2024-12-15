def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []  # Convex hull is not possible with less than 3 points

    hull = []

    l = min(range(n), key=lambda i: points[i][0])  # Leftmost point
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break

    return hull

points = [(0, 0), (1, 1), (2, 2), (2, 0), (3, 1), (3, 3), (0, 3)]
hull = convex_hull(points)

print("Convex Hull:", hull)








