from typing import List
import bisect

def LIS(arr: List[int]) -> int:
    """Returns the length of the longest strictly increasing subsequence of arr"""
    seq = []

    for i in range(len(arr)):
        t = bisect.bisect_left(seq, arr[i])
        if t == len(seq):
            seq.append(arr[i])
        else:
            seq[t] = arr[i]

    return len(seq)


def LIS_dp(arr: List[int]) -> List[int]:
    """Returns the length of the longest strictly increasing subsequence of arr[:i + 1]"""
    seq = []
    prev = [-1] * len(arr) #previous element to element i in the subseq

    for i in range(len(arr)):
        t = bisect.bisect_left(seq, (arr[i], 0))
        if t == len(seq):
            seq.append((arr[i], i))
        else:
            seq[t] = (arr[i], i)
        if t > 0:
            prev[i] = seq[t - 1][1]

    for i in range(len(prev)):
        if prev[i] == -1:
            prev[i] = 1
        else:
            prev[i] = prev[prev[i]] + 1

    return prev


def LIS_arr(arr: List[int]) -> List[int]:
    """Returns a longest strictly increasing subsequence of arr"""
    seq = []
    prev = [-1] * len(arr) #previous element to element i in the subseq

    for i in range(len(arr)):
        t = bisect.bisect_left(seq, (arr[i], 0))
        if t == len(seq):
            seq.append((arr[i], i))
        else:
            seq[t] = (arr[i], i)
        if t > 0:
            prev[i] = seq[t - 1][1]

    out = []
    ind = seq[-1][1]
    while ind != -1:
        out.append(arr[ind])
        ind = prev[ind]
    out.reverse()
    return out


def LIS_count(arr: List[int]) -> int:
    """Returns the number of longest strictly increasing subsequences of arr"""
    class BIT:
        def __init__(self, n: int) -> None:
            self.bit = [[0, 0] for _ in range(n)]

        def update(self, idx: int, x: int) -> None:
            """updates the element at idx by x"""
            while idx < len(self.bit):
                self.bit[idx] = max(self.bit[idx], x)
                idx |= idx + 1  # gets the parent of element i

        def query(self, end: int) -> int:
            """calc f on the range [0, end)"""
            x = [float('-inf'), 0]
            while end:
                x = max(x, self.bit[end - 1])
                end &= end - 1  # gets the next block for calculating the query
            return x
