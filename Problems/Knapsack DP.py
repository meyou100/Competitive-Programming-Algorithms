from typing import List
from collections import deque

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> List[int]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element can only be used once. Follow the comments for choose weights s.t. sum(weights) <= capacity
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1) #make default value False
    #dp[0] = True

    for i in range(len(values)):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i]) #|= dp[j - weights[i]]

    return dp


def knapsack_complete(weights: List[int], values: List[int], capacity: int) -> List[int]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element can be used multiple times
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp


def knapsack_mult(weights: List[int], values: List[int], uses: List[int], capacity: int) -> List[int]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element i can be used uses[i] times
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        if not weights[i]:
            for j in range(len(dp)):
                dp[j] += values[i] * uses[i]
                continue

        for mod in range(weights[i]):
            dq = deque()
            for div in range((capacity - mod) // weights[i] + 1):
                G_q = dp[div * weights[i] + mod] - values[i] * div
                #pop everything outside the window
                while dq and dq[0][0] < div - uses[i]:
                    dq.popleft()

                #Pops all elements that are worse than the current G value from the back
                while dq and dq[-1][1] <= G_q:
                    dq.pop()

                dq.append((div, G_q))
                dp[div * weights[i] + mod] = dq[0][1] + values[i] * div

    return dp


def fast_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Easily adapted to multiple knapsack by duplicating a weight and value pair k times
    O(n * max(weights)) time O(max(weights)) space"""
