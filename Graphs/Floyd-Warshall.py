from typing import List

#Implements the Floyd-Warshall Algorithm for finding the shortest path between any 2 nodes
#Notes: modifies in-place, accepts an adjacency matrix as an argument
def FloydWarshall(dist: List[List[int | float]]) -> None:
    #dist must be an adjacency matrix for the graph, float('inf') for no edge, 0 nodes mapping to themselves, positive number for edge weights
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
