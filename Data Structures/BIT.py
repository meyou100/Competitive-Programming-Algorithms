from typing import List

class BIT:
    def __init__(self, x: List[int]) -> None:
        """transform list into BIT"""
        self.bit = x[:]
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                self.bit[j] += self.bit[i]

    def update(self, idx: int, x: int) -> None:
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end: int) -> int:
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k: int) -> int:
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1