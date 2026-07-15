from typing import List, Tuple

#Implements the linear Sieve of Eratosthenes for finding all primes less than or equal to n
#Note: O(n) but generally slower than the normal sieve
def LinearSieve(n: int) -> Tuple[List[int], List[bool]]:
    composite = [False] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if not composite[i]:
            prime.append(i)
        for j in range(len(prime)):
            if i * prime[j] > n:
                break
            composite[i * prime[j]] = True
            if not i % prime[j]:
                break
    return prime, composite
