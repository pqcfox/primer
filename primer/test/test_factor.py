from ..factor import trial 

import pytest

class TestTrialDivision:
    passing = [(2,      {2: 1}),
               (17,     {17: 1}),
               (384,    {2: 7, 3: 1}),
               (29483,  {29483: 1}),
               (583928, {2: 3, 47: 1, 1553: 1})]

    failing = [-238.3, -39, -23/2, 0, 1]

    @pytest.mark.parametrize("input,expected", passing)
    def test_passing(self, input, expected):
        assert trial(input) == expected

    @pytest.mark.parametrize("input", failing)
    def test_value_error(self, input):
        with pytest.raises(ValueError):
            trial(input)
