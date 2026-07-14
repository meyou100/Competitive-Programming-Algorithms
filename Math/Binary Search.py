from typing import Callable

#Implements binary search on the answer with relative and absolute error
#Conditions:
#answer function must be monotonic
#the check function should run in around O(n) time
#check returns true if the float is an answer or false otherwise
def BinarySearch(left: float, right: float, check: Callable[[float], bool], epsilon: float = float(1e-6)):
    def absBinSearch(l: float, r: float, c: Callable[[float], bool], e: float):
        while r - l > epsilon:
            mid = (l + r) / 2
            if check(mid):
                r = mid
            else:
                l = mid
    def relBinSearch(l: float, r: float, c: Callable[[float], bool], e: float):

    if check(1): #if the answer is smaller than 1, abs binary search is better
        return absBinSearch(left, right, check, epsilon)
    else: # if the answer is greater than 1, rel binary search is better
        return relBinSearch(left, right, check, epsilon)