from typing import List
import heapq
from Data_Structures.DSU import *

def kruskal(edges: List[List[int]], nodes: int) -> int:
    """Kruksal's Algorithm for min spanning tree
    Returns -1 if the graph isn't connected"""
    heap = edges[:] #don't need if edges can be mutated
    heapq.heapify(heap)
    dsu = DSU(nodes)
    res = 0

    while heap:
        edge = heapq.heappop(heap)
        if dsu.find(edge[0]) != dsu.find(edge[1]):
            dsu.union(edge[0], edge[1])
            res += edge[2]
            if dsu.set_size(edge[0]) == nodes:
                return res

    return -1