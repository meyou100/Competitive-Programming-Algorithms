from typing import List

def maxDist(points: List[List[int]]) -> float:
    """Rotating by 45 degrees clockwise around the origin and scaling by sqrt(2) allows for manhattan distance to be computed as
    max(|x1' - x2'|, |y1' - y2'|). Here we use this to find the max distance between any 2 points in the list.
    O(n) time O(1) space"""
    if len(points) < 2:
        return 0

    maxu = maxv = float('-inf')
    minu = minv = float('inf')
    for p in points:
        u, v = p[0] + p[1], p[1] - p[0]
        maxu = max(maxu, u)
        minu = min(minu, u)
        maxv = max(maxv, v)
        minv = min(minv, v)
    return max(maxu - minu, maxv - minv)