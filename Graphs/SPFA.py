from collections import deque
from typing import List, Tuple

#Implements the shortest path faster algorithm that can deal with negative edge weights and find a negative cycle
#Note: generally faster than Bellman-Ford but slower in the worst case (negative cycles, etc.) due to high constant factor
def SPFA(adj: List[List[Tuple[int, int] | List[int]]], start: int) -> bool | List[int | float]:
    q = deque([start])
    dist = [float('inf')] * len(adj) #holds the min distance from start to any node
    inqueue = [False] * len(adj) #prevents adding a node that is already in the queue
    inqueue[start] = True
    dist[start] = 0
    count = [0] * len(adj) #counts the number of times the shortest distance to a node is updated

    while q:
        vertex = q.pop()
        inqueue[vertex] = False
        for edge in adj[vertex]:
            if dist[vertex] + edge[1] < dist[edge[0]]:
                dist[edge[0]] = dist[vertex] + edge[1]

                if not inqueue[edge[0]]:
                    inqueue[edge[0]] = True
                    q.append(edge[0])
                    count[edge[0]] += 1
                    if count[edge[0]] > len(adj):
                        return False #negative cycle
    return dist
