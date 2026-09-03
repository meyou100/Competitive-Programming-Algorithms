import operator
from typing import List, Callable

class BIT:
    def __init__(self, x: List[int], f: Callable[[int, int], int]=operator.add, g: Callable[[int, int], int]=operator.sub, identity: int=0) -> None:
        """transform list into BIT"""
        self.bit = x[:]
        self.f = f #group operation
        self.g = g #inverse operation
        self.identity = identity #identity in the group
        for i in range(len(x)):
            j = i | (i + 1) #gets the parent of element i
            if j < len(x):
                self.bit[j] = self.f(self.bit[j], self.bit[i]) #updates the parent with element i

    def update(self, idx: int, x: int) -> None:
        """updates the element at idx by x"""
        while idx < len(self.bit):
            self.bit[idx] = self.f(self.bit[idx], x)
            idx |= idx + 1 #gets the parent of element i

    def _prefix(self, end: int) -> int:
        """calc f on the range [0, end)"""
        x = self.identity
        while end:
            x = self.f(x, self.bit[end - 1])
            end &= end - 1 #gets the next block for calculating the query
        return x

    def query(self, start: int, end: int) -> int:
        """calc f on the range [start, end)"""
        return self.g(self._prefix(end), self._prefix(start))

    def findkth(self, k: int) -> int:
        """Find largest idx such that sum(bit[:idx]) <= k. the list must have no negative numbers and f = +"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1