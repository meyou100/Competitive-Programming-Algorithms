import math
from typing import List, Tuple, Callable

def sieve(n: int) -> List[bool]:
    """Returns a list which indicates whether numbers <= n are prime
    Generally faster than linear sieve due to constant factors
    O(nlog(log(n))) time O(n) space"""
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  #0 and 1 aren't prime
    for i in range(2, math.isqrt(n) + 1):
        if prime[i]:
            prime[i*i::i] = [False] * (n // i + 1 - i)
    return prime

def linearSieve(n: int) -> Tuple[List[int], List[int]]:
    """Returns a list of primes up to n and a list containing the smallest prime factor of i for each i
    Primality can be checked as spf[i] == i
    Generally slower than normal sieve
    O(n) time O(n) space"""
    spf = [0] * (n + 1) #smallest prime factor
    spf[0] = 2 #smallest prime factor of 0 is 2
    prime = []
    for i in range(2, n + 1):
        if not spf[i]:
            spf[i] = i
            prime.append(i)
        for p in prime:
            if p > spf[i] or i * p > n:
                break
            spf[i * p] = p
    return prime, spf

def spfSieve(n: int) -> List[int]:
    """Returns a list spf where spf[i] is the smallest prime factor of i
    O(nlog(log(n))) time O(n) space"""
    spf = [0] * (n + 1) #smallest prime factor
    spf[0] = 2 #smallest prime factor of 0 is 2
    for i in range(2, n + 1):
        if not spf[i]:
            spf[i] = i
            for j in range(i * i, n + 1, i):
                if not spf[j]:
                    spf[j] = i
    return spf
def factorize(n: int, spf: List[int]) -> List[int]:
    """Factorize n into prime factors given the smallest prime factors list
    O(log(n)) time O(log(n)) space"""
    factorization = []
    while n > 1:
        factorization.append(spf[n])
        n //= spf[n]
    return factorization

def calcMultFunc(n: int, spf: List[int], func: Callable[[int, int], int]) -> int:
    """Calculates the multiplicative function on n
    func(a, b) = func(a ^ b)
    O(log(n) * f) time O(1) space"""
    out = 1
    while n > 1:
        c = 0 #exponent of the prime factor
        p = spf[n]
        while not n % p:
            n //= p
            c += 1
        out *= func(p, c)
    return out

def calcTotalMultFuncLin(n: int, func: Callable[[int, int], int]) -> List[int]:
    """Calculates the multiplicative function for all numbers <= n
    func(a, b) = func(a ^ b)
    O(n * f) time O(n) space"""
    f = [0] * (n + 1)
    exponent = [0] * (n + 1) #the largest exponent of spf[i] that divides i
    power = [0] * (n + 1) #spf[i] ** exponent[i]
    primes = []
    f[1] = 1
    for i in range(2, n + 1):
        if not exponent[i]: #i is prime
            exponent[i] = 1
            power[i] = i
            primes.append(i)
            f[i] = func(i, 1)

        for p in primes:
            j = p * i
            if j > n:
                break
            if i % p: #i doesn't share a prime factor with p
                exponent[j] = 1
                power[j] = p
                f[j] = f[i] * f[p]
            else:
                exponent[j] = exponent[i] + 1
                power[j] = power[i] * p
                if power[j] == j: #j is a prime power, compute the function on j
                    f[j] = func(p, exponent[j])
                else: #j isn't solely a prime power so the values needed have already been computed
                    f[j] = f[j // power[j]] * f[power[j]]
                break
    return f

def calcTotalMultFunc(n: int, spf: List[int], func: Callable[[int, int], int]) -> List[int]:
    """Calculates the multiplicative function for all numbers <= n given an spf array
    func(a, b) = func(a ^ b)
    Only fails on the 0 function f(x) = 0
    O(n * f) time O(n) space"""
    f = [0] * (n + 1)
    exponent = [0] * (n + 1) #the largest exponent of spf[i] that divides i
    power = [0] * (n + 1) #spf[i] ** exponent[i]
    f[1] = 1
    for i in range(2, n + 1):
        p = spf[i]
        j = i // p
        if j % p: #j doesn't share any prime factor with p
            exponent[i] = 1
            power[i] = p
        else:
            exponent[i] = exponent[j] + 1
            power[i] = power[j] * p

        if power[i] == i: #i is a prime power, compute the function on i
            f[i] = func(p, exponent[i])
        else: #i isn't a prime power so the values needed have already been computed
            f[i] = f[i // power[i]] * f[power[i]]
    return f

def segmentedSieve(left: int, right: int) -> List[bool]:
    """Calculates the primes in the window from left to right
    This is useful for reasonable window sizes but large values for left and right
    O(sqrt(right)log(log(sqrt(right))) + (right - left)log(log(right)))"""
    rsqrt = math.isqrt(right) + 1
    prime = [True] * rsqrt
    primes = [2]
    #calculate primes up to sqrt(right)
    for i in range(3, rsqrt, 2):
        if prime[i]:
            primes.append(i)
            for j in range(i * i, rsqrt, i * 2):
                prime[j] = False

    window = [True] * (right - left + 1)
    for p in primes:
        for j in range(max(p, (left - 1) // p + 1) * p, right + 1, p):
            window[j - left] = False
    #edge case where 0 and 1 are in the window
    for x in range(left, min(right + 1, 2)):
        window[x - left] = False
    return window
