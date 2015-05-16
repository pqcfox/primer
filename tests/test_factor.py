from primer.factor import trial 

import pytest

class TestTrialDivision:
    def test_working_cases(self):
        tests = {2:      {2: 1},
                 17:     {17: 1},
                 384:    {2: 7, 3: 1},
                 29483:  {29483: 1},
                 583928: {2: 3, 47: 1, 1553: 1}}

        for n in tests:
            assert dict(trial(n)) == tests[n]

    def test_value_error(self):
        tests = [-23, 0, 1, 295.3, 5/3]

        for n in tests:
            with pytest.raises(ValueError):
                trial(n)
