from .utils import eratosthenes

import collections
import math

def trial(n, sieve=True):
    factors = collections.Counter() 
    divisors = list(range(2, upper)) if sieve else eratosthenes(upper) 

    for d in divisors:
        while n % d == 0:
            n //= d
            factors[d] += 1

    return factors
