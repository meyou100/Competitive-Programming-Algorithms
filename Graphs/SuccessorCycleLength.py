from typing import List

def floyd(adj: List[int]) -> int:
    """Finds the cycle length in a successor graph
    O(n) time O(1) space"""
    slow, fast = adj[0], adj[adj[0]]

    while slow != fast:
        slow = adj[slow]
        fast = adj[adj[fast]]

    fast = adj[fast]
    size = 1
    while slow != fast:
        fast = adj[fast]
        size += 1

    return size