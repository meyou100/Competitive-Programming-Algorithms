from typing import List

def maxPathLength(adj: List[List[int]]) -> List[int]:
    """Returns a list of the longest path starting at each node of the tree
    Note: the graph must be connected (a tree not a forest)"""
    n = len(adj)
    parent = [0] * n
    top_order = []
    stack = [0]
    parent[0] = -1

    while stack:
        x = stack.pop()
        top_order.append(x)
        for y in adj[x]:
            if y != parent[x]:
                parent[y] = x
                stack.append(y)

    max_length = [[0, 0] for _ in range(n)]
    for x in reversed(top_order):
        for y in adj[x]:
            if y == parent[x]:
                continue
            length = max_length[y][0] + 1
            if length > max_length[x][0]:
                max_length[x][0], max_length[x][1] = length, max_length[x][0]
            elif length > max_length[x][1]:
                max_length[x][1] = length

    for x in top_order:
        if parent[x] == -1:
            continue
        if max_length[parent[x]][0] == max_length[x][0] + 1:
            length = max_length[parent[x]][1] + 1
        else:
            length = max_length[parent[x]][0] + 1
        if length > max_length[x][0]:
            max_length[x][0], max_length[x][1] = length, max_length[x][0]
        elif length > max_length[x][1]:
            max_length[x][1] = length

    return [l[0] for l in max_length]

print(maxPathLength([[], [2], [], []]))