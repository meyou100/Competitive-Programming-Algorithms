from typing import List, Tuple
import heapq

#Implements Dijkstra's algorithm for finding the shortest path between a starting node to all other nodes
def Dijkstra(adj: List[List[Tuple[int, int]]], n: int, start: int):  #adjacency list, number of nodes, and start node
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
