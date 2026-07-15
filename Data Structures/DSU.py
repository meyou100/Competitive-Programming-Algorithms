class DSU:
    def __init__(self, n: int) -> None:
        self.nodes = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    #Implementation using recursion is slower
    def find(self, a: int) -> int:
        acopy = a
        while a != self.nodes[a]:
            a = self.nodes[a]
        while acopy != a:
            self.nodes[acopy], acopy = a, self.nodes[acopy]
        return a

    def union(self, a:int , b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a != b:
            self.num_sets -= 1
            if self.size[a] > self.size[b]:
                self.nodes[b] = a
                self.size[a] += self.size[b]
            else:
                self.nodes[a] = b
                self.size[b] += self.size[a]

    def __len__(self) -> int:
        return self.num_sets

    def __repr__(self) -> str:
        return str(self.nodes)
