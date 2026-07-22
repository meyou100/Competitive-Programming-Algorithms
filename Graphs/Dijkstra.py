from typing import List, Tuple
import heapq

#Implements Dijkstra's algorithm for finding the shortest path between a starting node to all other nodes
#Fails if there are negative weights
#If provided with the parameter p=True, it will return a parent array representing the direct parent of a node in the shortest path
def Dijkstra(adj: List[List[Tuple[int, int] | List[int]]], start: int, p: bool=False) -> List[int | float] | Tuple[List[int | float], List[int]]:  #adjacency list, and start node
    n = len(adj)
    if p: #if the parent array is requested
        parent = [-1] * n
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
                if p:
                    parent[nxt] = cur

    if p:
        return dist, parent
    return dist

#Builds the shortest path from the start node to the given end node
def get_path(parent: List[int], end: int) -> List[int]:
    path = []
    while parent[end] != -1:
        path.append(end)
        end = parent[end]
    path.append(end) #append the start node
    path.reverse() #the path was built backwards
    return path