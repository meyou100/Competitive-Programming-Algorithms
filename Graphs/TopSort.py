from collections import deque
from typing import List

def kahn(n: int, adj: List[List[int]]) -> List[int]:
    """Returns a topological sort of the directed graph or an empty list if there's a cycle
    O(m + n) time O(n) space"""
    #calculate the indegree of each node
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1

    queue = deque(i for i in range(n) if not indeg[i])
    out = []

    while queue:
        u = queue.popleft()
        out.append(u)
        #removing u from the graph by removing all its edges
        for v in adj[u]:
            indeg[v] -= 1
            #if v has no incoming edges it is added to the queue to be processed after the
            if not indeg[v]:
                queue.append(v)

    return out #if len(out) == n else [] #fewer than n nodes means a cycle