from typing import List, Callable

class SegTree:
    def __init__(self, data: List[float], identity: float=float('-inf'), func: Callable[[float, float], float]=max) -> None:
        """Initializes the seg tree with data
        Uses 1-based indexing. 0 has no meaning"""
        self.identity = identity
        self.func = func
        self.n = len(data)
        self.size = 1 << (len(data) - 1).bit_length() #make the tree size a power of 2

        self.tree = [identity] * (2 * self.size)
        self.tree[self.size:self.size + len(data)] = data

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx: int, val: float, func: Callable[[float, float], float] | None=None) -> None:
        """Updates val to idx with the specified func"""
        idx += self.size
        if func is None:
            self.tree[idx] = self.func(self.tree[idx], val)
        else:
            self.tree[idx] = func(self.tree[idx], val)
        self._update(idx)

    def set(self, idx: int, val: float) -> None:
        """Sets idx to val"""
        idx += self.size
        self.tree[idx] = val
        self._update(idx)

    def _update(self, idx: int) -> None:
        """Propagates updates through the tree"""
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def query(self, left: int, right: int) -> float:
        """Calc func on the range [left, right)"""
        if left < 0 or right > self.n:
            raise ValueError("Invalid range")
        left += self.size
        right += self.size - 1
        lres, rres = self.identity, self.identity #compute the left and right side separately so that func doesn't have to be commutative
        while left <= right:
            if left % 2:
                lres = self.func(lres, self.tree[left])
                left += 1
            if not right % 2:
                rres = self.func(rres, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        return self.func(lres, rres)

    def __len__(self) -> int:
        return self.n

    def __repr__(self) -> str:
        return f"SegTree({self.tree})"