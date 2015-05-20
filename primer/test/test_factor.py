from ..factor import trial, fermat

import pytest

trial_values = [(2,      {2: 1}),
                (17,     {17: 1}),
                (384,    {2: 7, 3: 1}),
                (29483,  {29483: 1}),
                (583928, {2: 3, 47: 1, 1553: 1})]

@pytest.mark.parametrize("n,expected", trial_values)
def test_passing(n, expected):
    assert trial(n) == expected

fermat_values = [(15,   (3, 5)),
                 (119,  (7, 17)),
                 (219,  (3, 73)),
                 (5959, (59, 101))]

@pytest.mark.parametrize("n,expected", fermat_values)
def test_fermat(n, expected):
    assert fermat(n) == expected
