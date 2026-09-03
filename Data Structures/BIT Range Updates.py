import operator
from typing import List, Callable

class RangeUpdateBIT:
    def __init__(self, x: List[int], f: Callable[[int, int], int]=operator.add, g: Callable[[int, int], int]=operator.sub, identity: int=0) -> None:
        """transform list into BIT. list shouldn't be a difference array"""
        self.bit = [x[0]] + [g(x[i + 1], x[i]) for i in range(len(x) - 1)] #create difference array
        self.f = f #group operation
        self.g = g #inverse operation
        self.identity = identity #identity in the group
        for i in range(len(x)):
            j = i | (i + 1) #gets the parent of element i
            if j < len(x):
                self.bit[j] = self.f(self.bit[j], self.bit[i])

    def _point_update(self, idx: int, x: int) -> None:
        """updates the element at idx by x"""
        while idx < len(self.bit):
            self.bit[idx] = self.f(self.bit[idx], x)
            idx |= idx + 1 #gets the parent of element i

    def update(self, start: int, end: int, x: int) -> None:
        """updates the range [l, r) by x"""
        self._point_update(start, x)
        self._point_update(end, self.g(self.identity, x))

    def query(self, idx: int) -> int:
        """calculates the element at index idx"""
        idx += 1 #includes the idx in the range
        x = self.identity
        while idx:
            x = self.f(x, self.bit[idx - 1])
            idx &= idx - 1 #gets the next block for calculating the query
        return x

    def findkth(self, k: int) -> int:
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k = self.g(k, self.bit[idx])
        return idx + 1