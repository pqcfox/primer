import functools
import math
import operator

def bound(n):
    """Accepts a number and requires it to be greater than 2."""
    if n < 2:
        raise ValueError('n must be greater than or equal to 2')
    return int(n)
