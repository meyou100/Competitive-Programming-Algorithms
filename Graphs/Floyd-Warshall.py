from typing import List

#Implements the Floyd-Warshall Algorithm for finding the shortest path between any 2 nodes
#Notes: modifies in-place, accepts an adjacency matrix as an argument, fails if there's a negative cycle
def FloydWarshall(dist: List[List[int | float]]) -> None:
    #dist must be an adjacency matrix for the graph, float('inf') for no edge, 0 nodes mapping to themselves, positive number for edge weights
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

#Checks if the graph has a negative cycle and fixes the output of the Floyd-Warshall
#Note: modifies in-place
def check_negative_cycle(dist: List[List[int | float]]) -> None:
    n = len(dist)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] != float('inf') and dist[k][k] < 0 and dist[k][j] != float('inf'):
                    #dist[k][k] < 0 means that this node is part of a negative cycle
                    dist[i][j] = float('-inf')

