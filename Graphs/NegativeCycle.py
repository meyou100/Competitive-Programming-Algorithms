from typing import List, Tuple

#Implements the Bellman-Ford Algorithm to find a negative cycle, not necessarily all of them
def NegativeCycle(edges: List[Tuple[int, int, int] | List[int]], num_nodes: int=-1) -> List[int] | bool:
    if num_nodes == -1:
        num_nodes = max(map(lambda a: max(a[0], a[1]), edges)) + 1 #0 is also a node

    dist = [0] * num_nodes #initialize all distances to 0
    parent = [-1] * num_nodes #holds the parent node in the shortest path
    for i in range(num_nodes):
        last = -1 #the last updated node in a cycle
        for edge in edges:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                parent[edge[1]] = edge[0]
                last = edge[1]
        if last == -1:
            return False #no negative cycle

    for _ in range(num_nodes):
        last = parent[last] #last may not be directly in the negative cycle but reachable from it

    cycle = []
    vertex = last
    while vertex != last or len(cycle) < 1:
        cycle.append(vertex)
        vertex = parent[vertex]
    return list(reversed(cycle))