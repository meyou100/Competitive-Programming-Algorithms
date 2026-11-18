from typing import List, Callable, Tuple
import operator

class HLD:
    def __init__(self, adj: List[List[int]], root: int=0, val_edges=False, identity: float=0, func: Callable[[float, float], float]=operator.add) -> None:
        """Initializes the HLD object
        val_edges is True when the values are on edges and False if on nodes
        root is the root of the tree
        identity matches the identity of the set the BIT/Seg Tree/other works over
        func is the function the BIT/Seg Tree/other uses
        func must be commutative and associative"""
        n = len(adj)
        self.vals_edges = 1 if val_edges else 0
        self.identity = identity
        self.func = func
        parent = [-1] * n
        top_order = []
        stack = [root]
        while stack:
            node = stack.pop()
            top_order.append(node)
            for child in adj[node]:
                if child != parent[node]:
                    parent[child] = node
                    stack.append(child)

        size = [1] * n
        for node in reversed(top_order):
            if parent[node] != -1:
                size[parent[node]] += size[node]

        heavy = [-1] * n #points to the heavy child
        for node in top_order:
            par = parent[node]
            if par != -1 and (heavy[par] == -1 or size[node] > size[heavy[par]]):
                heavy[par] = node

        top_of_chain = [0] * n
        label = [0] * n
        time = 0
        top_of_chain[root] = root
        stack = [root]
        while stack:
            node = stack.pop()
            label[node] = time
            time += 1
            for child in adj[node]:
                if child != parent[node] and child != heavy[node]:
                    top_of_chain[child] = child
                    stack.append(child)
            if heavy[node] != -1:
                top_of_chain[heavy[node]] = top_of_chain[node]
                stack.append(heavy[node])

        self.parent, self.size, self.top_of_chain, self.label, self.root = parent, size, top_of_chain, label, root

    def values(self, values: List[int]) -> List[float]:
        """Returns the array to make the BIT/Seg Tree/other array over"""
        n = len(values)
        arr = [self.identity] * n
        for v in range(n):
            arr[self.label[v]] = values[v]
        if self.vals_edges:
            arr[self.label[self.root]] = self.identity  # root has no parent edge
        return arr

    def _process(self, u: int, v: int, func: Callable[[int, int], None]) -> None:
        top_of_chain, label, parent = self.top_of_chain, self.label, self.parent
        while top_of_chain[u] != top_of_chain[v]:
            if label[top_of_chain[u]] > label[top_of_chain[v]]:
                u, v = v, u
            func(label[top_of_chain[v]], label[v] + 1)
            v = parent[top_of_chain[v]]
        if label[u] > label[v]:
            u, v = v, u
        func(label[u] + self.vals_edges, label[v] + 1)

    def _subtree_range(self, node: int) -> Tuple[int, int]:
        return self.label[node] + self.vals_edges, self.label[node] + self.size[node]

    def update_path(self, u: int, v: int, update: Callable[[int, int], None]) -> None:
        """Updates nodes on the path from u to v
        update must take in a range [l, r) and update the values of the nodes on the path
        O(log^2(n)) time for seg tree/BIT"""
        self._process(u, v, update)

    def query_path(self, u: int, v: int, query: Callable[[int, int], float]) -> float:
        """Queries the value of the path from u to v
        query must take in a range [l, r) and query the values of the nodes on the path
        O(log^2(n)) time for seg tree/BIT"""
        result = self.identity
        def op(l: int, r: int) -> None:
            nonlocal result
            result = self.func(result, query(l, r))
        self._process(u, v, op)
        return result

    def update_subtree(self, root: int, update: Callable[[int, int], None]) -> None:
        """Updates all nodes in the subtree rooted at root
        update must take in a range [l, r) and update the values of the nodes in the subtree
        O(log(n)) time for seg tree/BIT"""
        update(*self._subtree_range(root))

    def query_subtree(self, root: int, query: Callable[[int, int], float]) -> float:
        """Queries the value of the nodes in the subtree rooted at root
        query must take in a range [l, r) and query the values of the nodes in the subtree
        O(log(n)) time for seg tree/BIT"""
        return query(*self._subtree_range(root))
