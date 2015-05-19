import functools
import math
import operator

def bound(n):
    """Accepts a number and requires it to be greater than 2."""
    if n < 2:
        raise ValueError('n must be greater than or equal to 2')
    return int(n)

def sieve_to_primes(sieve):
    """Accepts a zero-indexed sieve and returns all primes found."""
    primes = []
    for i in range(len(sieve)):
        if sieve[i]:
            primes.append(i)

    return primes

def eratosthenes(n):
    """Returns all primes in [2, n] using the Sieve of Eratosthenes."""
    n = bound(n)
    sieve = [True] * (n - 1) # represents 2 through n 
    for d in range(2, int(math.sqrt(n)) + 1):
        focus = 2 * d 
        while focus <= n:
            sieve[focus - 2] = False
            focus += d

    zero_indexed_sieve = 2 * [False] + sieve
    return sieve_to_primes(zero_indexed_sieve) 

def wheel(n, basis):
    """Returns a relatively prime set in [2, n] using the Wheel Algorithm."""
    n = bound(n)
    size = functools.reduce(operator.mul, basis)
    wheel = []
    for x in range(0, n + size, size):
        wheel.append([True] * size)
    
    inside = wheel[0]
    prime_spokes = [p - 1 for p in basis] # subtract one for zero-indexing
    mults = [k for k in range(1, size + 1) if any([k % p == 0 for p in basis])]
    mult_spokes = [mult - 1 for mult in mults if mult not in basis]
    wheel[0][0] = False
     
    for x in range(len(wheel)):
        spokes = mult_spokes
        if x != 0:
            spokes.extend(prime_spokes)
        if x == 0:
            pass
        for spoke in spokes:
            wheel[x][spoke] = False

    flat_wheel = [False] + [value for circle in wheel for value in circle]
    return [k for k in sieve_to_primes(flat_wheel) if k <= n]

print(wheel(20, [2, 3]))
