from typing import List

def Andrew(points: List[List[int]]) -> List[List[int]]:
    """Andrew's Algorithm for finding the convex hull of points
    Points on the edge of the hull between 2 other points are included
    O(nlogn) time O(n) space"""
    def cross(start: List[int], end1: List[int], end2: List[int]) -> int:
        """Computes the magnitude of the cross product of 2D vectors starting at start and ending at end1 and end2"""
        return (end1[0] - start[0]) * (end2[1] - start[1]) - (end2[0] - start[0]) * (end1[1] - start[1])

    if len(points) <= 2:
        return points

    #edge case where all points are collinear
    a, b = points[0], points[1]
    if all(not cross(a, b, p) for p in points):
        return points

    points.sort()
    out = []
    last_hull = 0 #size of the lower hull once the first loop finishes
    for _ in range(2): #construct the lower then upper hull
        for i in range(len(points)):
            #pops all elements from the hull that make it non convex
            while len(out) >= last_hull + 2 and cross(out[-2], out[-1], points[i]) < 0:
                out.pop()
            out.append(points[i])

        out.pop()
        last_hull = len(out)
        points.reverse() #go in reverse order for the upper hull
    return out