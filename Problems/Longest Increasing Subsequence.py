from typing import List
import bisect

def LIS(arr: List[int]) -> int:
    """Returns the length of the longest strictly increasing subsequence of arr
    O(nlogn) time O(ans) space"""
    seq = []

    for i in range(len(arr)):
        t = bisect.bisect_left(seq, arr[i])
        if t == len(seq):
            seq.append(arr[i])
        else:
            seq[t] = arr[i]

    return len(seq)


def LIS_dp(arr: List[int]) -> List[int]:
    """Returns the length of the longest strictly increasing subsequence of arr[:i + 1]
    O(nlogn) time O(n) space"""
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
    """Returns a longest strictly increasing subsequence of arr
    O(nlogn) time O(n) space"""
    if not arr:
        return []

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


def LIS_count(arr: List[int]) -> List[float | int]:
    """Returns the length and number of longest strictly increasing subsequences of arr
    O(nlogn) time O(max(arr)) space"""
    if not arr:
        return [0, 1]

    class BIT:
        def __init__(self, n: int) -> None:
            self.bit = [[0, 0] for _ in range(n)]

        def update(self, idx: int, x: int, count: int) -> None:
            while idx < len(self.bit):
                if self.bit[idx][0] < x:
                    self.bit[idx] = [x, count]
                elif self.bit[idx][0] == x:
                    self.bit[idx][1] += count
                idx |= idx + 1  # gets the parent of element i

        def query(self, end: int) -> List[float | int]:
            x = [0, 1]
            while end:
                if self.bit[end - 1][0] > x[0]:
                    x = self.bit[end - 1][:]
                elif self.bit[end - 1][0] == x[0]:
                    x[1] += self.bit[end - 1][1]
                end &= end - 1  # gets the next block for calculating the query
            return x

    b = BIT(max(arr)) #assumes all values are positive
    for i in range(len(arr)):
        t = b.query(arr[i] - 1)
        t[0] += 1
        b.update(arr[i] - 1, t[0], t[1])

    return b.query(max(arr))