from ..factor import trial

import pytest

trial_values = [(2,      {2: 1}),
                (17,     {17: 1}),
                (384,    {2: 7, 3: 1}),
                (29483,  {29483: 1}),
                (583928, {2: 3, 47: 1, 1553: 1})]

@pytest.mark.parametrize("n,expected", trial_values)
def test_passing(n, expected):
    assert trial(n) == expected
