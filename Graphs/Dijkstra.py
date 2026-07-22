from typing import List, Tuple
import heapq

#Implements Dijkstra's algorithm for finding the shortest path between a starting node to all other nodes
#Fails if there are negative weights
def Dijkstra(adj: List[List[Tuple[int, int] | List[int]]], start: int) -> List[int | float]:  #adjacency list, and start node
    n = len(adj)
    dist = [float('inf')] * n
    processed = [False] * n
    dist[start] = 0
    q = [(0, start)]  #min heap
    while q:
        z, cur = heapq.heappop(q)  #weight and current node
        if processed[cur]:
            continue
        processed[cur] = True
        for nxt, w in adj[cur]:  #next node and weight
            if dist[cur] + w < dist[nxt]:
                dist[nxt] = dist[cur] + w
                heapq.heappush(q, (dist[nxt], nxt))
    return dist
