import pytest

from ..utils import eratosthenes 

class TestEratosthenes:
    passing = [(2,  [2]), 
               (12, [2, 3, 5, 7, 11]),
               (15, [2, 3, 5, 7, 11, 13]),
               (23, [2, 3, 5, 7, 11, 13, 17, 19, 23])]

    failing = [-2395.3, -67/2, -23, 0, 1]

    @pytest.mark.parametrize("input,expected", passing)
    def test_passing(self, input, expected):
        assert eratosthenes(input) == expected 

    @pytest.mark.parametrize("input", failing)
    def test_failing(self, input):
        with pytest.raises(ValueError):
            eratosthenes(input)
