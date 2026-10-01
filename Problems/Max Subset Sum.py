from typing import List

def subset_01(weights: List[int], capacity: int) -> int:
    """Returns the max subset sum of weights <= capacity as a bitset
    Each element is used at most once
    O(nW) time O(W) space"""
    mask = (1 << (capacity + 1)) - 1
    bitset = 1 #sum 0 is reachable
    for weight in weights:
        bitset |= (bitset << weight) & mask
    return bitset

def subset_complete(weights: List[int], capacity: int) -> int:
    """Returns the max subset sum of weights <= capacity as a bitset
    Each element can be used infinitely many times
    O(nW * log(W)) time O(W) space"""
    mask = (1 << (capacity + 1)) - 1
    bitset = 1
    for weight in weights:
        if not weight:
            continue
        while weight < capacity:
            bitset |= (bitset << weight) & mask
            weight <<= 1
    return bitset

def subset_multiple(weights: List[int], uses: List[int], capacity: int) -> int:
    """Returns the max subset sum of weights <= capacity as a bitset
    Each element can be used uses[i] times
    O(nW * log(max(uses))) time O(W) space"""
    mask = (1 << (capacity + 1)) - 1
    bitset = 1
    for weight, count in zip(weights, uses):
        k = 1
        while count > 0:
            take = min(k, count)
            bitset |= (bitset << take * weight) & mask
            count -= take
            k <<= 1
    return bitset

def subset_fast(weights: List[int], capacity: int) -> int:
    """Calculates the max sum of elements in values such that the corresponding sum of weights <= capacity
    Easily adapted to multiple knapsack by duplicating a weight and value pair k times
    O(n * max(weights)) time O(max(weights)) space"""
    ind = cur_sum =0
    while ind < len(weights) and cur_sum + weights[ind] <= capacity:
        cur_sum += weights[ind]
        ind += 1

    if ind == len(weights):
        return cur_sum

    m = max(weights)
    window = [-1] * (2 * m) #window[0] is never used
    window[cur_sum - capacity + m] = ind

    for i in range(ind, len(weights)):
        old = window[:]
        for j in range(m):
            window[j + weights[i]] = max(window[j + weights[i]], old[j])

        for j in range(2 * m - 1, m, -1):
            for k in range(max(0, old[j]), window[j]):
                window[j - weights[k]] = max(window[j - weights[k]], k)

    ans = capacity
    while window[ans + m - capacity] < 0:
        ans -= 1
    return ans