import math
from typing import List

#Implements the Sieve of Eratosthenes for finding all primes less than or equal to n
#Note: O(nlog(log(n))) but generally faster than linear sieve
def Sieve(n: int) -> List[bool]:
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  #0 and 1 aren't prime
    for i in range(2, math.isqrt(n) + 1):
        if prime[i]:
            for j in range(2 * i, n + 1, i):
                prime[j] = False
    return prime