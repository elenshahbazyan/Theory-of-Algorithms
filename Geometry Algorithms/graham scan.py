import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def polar_angle(p0, p):
    return math.atan2(p[1] - p0[1], p[0] - p0[0])

def graham_scan(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.remove(p0)
    points.sort(key=lambda p: polar_angle(p0, p))
    
    hull = [p0, points[0], points[1]]
    
    for i in range(2, len(points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    
    return hull

points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3), (1, 2)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)







