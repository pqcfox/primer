import math

def eratosthenes(n):
    """Returns all primes up to and including n using the Sieve of Eratosthenes."""
    sieve = [True] * (n - 1) # represents 2 through n 
    for d in range(2, int(math.sqrt(n)) + 1):
        focus = 2 * d 
        while focus <= len(sieve):
            sieve[focus - 2] = False
            focus += d

    primes = []
    for i in range(len(sieve)):
        if sieve[i]:
            primes.append(i + 2)
    
    return primes
