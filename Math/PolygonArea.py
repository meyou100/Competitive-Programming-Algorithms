from typing import List

def area(points: List[List[float]]) -> float:
    """Implements the shoelace thm to calculate the area of a polygon with the given vertices
    Restrictions: The polygon must be simple, vertices must be listed in order, and points shouldn't be empty"""
    return abs(sum(points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1] for i in range(len(points) - 1)) + points[-1][0] * points[0][1] - points[0][0] * points[-1][1]) / 2