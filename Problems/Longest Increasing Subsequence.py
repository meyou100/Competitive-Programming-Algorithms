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
    """Returns the length of the longest strictly increasing subsequence of arr"""
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
