import pytest

from ..sieve import eratosthenes, wheel

eratosthenes_values = [(2,  [2]), 
                       (12, [2, 3, 5, 7, 11]),
                       (15, [2, 3, 5, 7, 11, 13]),
                       (23, [2, 3, 5, 7, 11, 13, 17, 19, 23])]

@pytest.mark.parametrize("n,expected", eratosthenes_values)
def test_eratosthenes(n, expected):
    assert eratosthenes(n) == expected 

wheel_values = [(8,  [2],       [2, 3, 5, 7]),
                (12, [2, 3],    [2, 3, 5, 7, 11]),
                (19, [2, 3, 5], [2, 3, 5, 7, 11, 13, 17, 19]),
                (32, [2, 3],    [2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31])]

@pytest.mark.parametrize("n,basis,expected", wheel_values)
def test_wheel(n, basis, expected):
    assert wheel(n, basis) == expected
