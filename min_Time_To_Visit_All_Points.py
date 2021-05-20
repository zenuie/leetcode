def minTimeToVisitAllPoints(points):
    total_time, last_pt = 0, points[0]
    for curr_pt in points:
        total_time += max(abs(curr_pt[0] - last_pt[0]), abs(curr_pt[1] - last_pt[1]))
        last_pt = curr_pt

    return total_time
