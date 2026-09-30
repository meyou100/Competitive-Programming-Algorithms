from typing import List
from collections import deque

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> List[int]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element can only be used once
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp

def knapsack_complete(weights: List[int], values: List[int], capacity: int) -> List[float]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element can be used multiple times
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        #unbounded solution
        if not weights[i] and values[i]:
            return [float('inf')] * (capacity + 1)
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp

def knapsack_mult(weights: List[int], values: List[int], uses: List[int], capacity: int) -> List[int]:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Each element i can be used uses[i] times
    O(nW) time and O(W) space"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        if not weights[i]: #if weight[i] == 0 then for any capacity we can take all these elements
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