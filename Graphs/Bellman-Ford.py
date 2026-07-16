from typing import List, Tuple

#Implements the Bellman-Ford algorithm for finding the shortest path with negative weights and negative cycles
#Note: usually slower than SPFA but lower constant factor
def BellmanFord(edges: List[Tuple[int, int, int] | List[int]], start: int, num_nodes: int = -1) -> List[int | float] | bool:
    #edges should be in the form [node 1, node 2, cost] denoting a one-way edge from node 1 to node 2
    if num_nodes == -1: #finds the number of nodes if not explicitly given
        num_nodes = max(map(lambda a: max(a[0], a[1]), edges)) + 1 #0 is also a node

    dist = [float('inf')] * num_nodes
    dist[start] = 0
    for i in range(num_nodes + 1):
        b = False
        for edge in edges:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                b = True

        if not b:
            break
    else:
        return False #negative cycle
    return dist