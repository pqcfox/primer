from .sieve import eratosthenes
from .utils import bound

import collections
import math

def trial(n, sieve=True):
    """Performs trial division to fully factor n."""
    n = bound(n) 
    factors = collections.Counter() 
    upper = int(math.sqrt(n))
    divisors = list(range(2, upper)) if sieve else eratosthenes(upper) 

    for d in divisors:
        while n % d == 0:
            n //= d
            factors[d] += 1

    if n > 1: 
        factors[n] += 1

    return factors


def fermat(n):
    """Utilizes Fermat's algorithm to factor n."""
    n = bound(n)
    a = int(math.ceil(math.sqrt(n)))
    b_squared = a ** 2 - n
    while math.sqrt(b_squared) % 1 != 0:
        a += 1
        b_squared = a ** 2 - n

    b = int(math.sqrt(b_squared))

    return (a - b, a + b)
