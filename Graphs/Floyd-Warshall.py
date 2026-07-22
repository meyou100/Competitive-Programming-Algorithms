from typing import List

#Implements the Floyd-Warshall Algorithm for finding the shortest path between any 2 nodes
#Notes: modifies in-place, accepts an adjacency matrix as an argument, fails if there's a negative cycle
#If p=True, it will return a 2D array representing the last vertex that improved the distance between nodes which is used to build the shortest path
def FloydWarshall(dist: List[List[int | float]], p: bool=False) -> None | List[List[int]]:
    #dist must be an adjacency matrix for the graph, float('inf') for no edge, 0 nodes mapping to themselves, positive number for edge weights
    n = len(dist)
    if p:
        inbetween = [[i if dist[i][j] != float('inf') else -1 for j in range(n)] for i in range(n)]
        print(inbetween)
    for k in range(n): #middle node
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if p:
                        inbetween[i][j] = k #parent represents the last vertex k that improved the distance between i and j

    if p:
        return inbetween

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

#Returns the shortest path from start to end
#Assumes check_negative_cycle(dist) is run first to deal with negative cycles
def get_path(dist: List[List[int | float]], inbetween: List[List[int]], start: int, end: int) -> List[int]:
    if dist[start][end] == float('inf') or dist[start][end] == float('-inf'):
        return [] #there is no shortest path between start and end
    if start == end: #the path is one node long
        return [start]

    path = [] #holds the shortest path between the nodes
    stack = [[start, end]] #iterative dfs to figure out the nodes in the path
    while stack:
        i, j = stack.pop()
        if inbetween[i][j] != i: #the path between i and j isn't direct
            stack.append([inbetween[i][j], j])
            stack.append([i, inbetween[i][j]])
        else:
            path.append(i)
    path.append(end)
    return path