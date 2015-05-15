import collections
import math

def trial(n, sieve=True):
    factors = collections.Counter() 
    # divisors = 
    for d in divisors:
        while n % d == 0:
            n //= d
            factors[d] += 1

    return factors
