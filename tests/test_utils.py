from primer.utils import eratosthenes 

class TestSieveOfEratosthenes:
    def test_working_cases(self):
        tests = {2:  [2], 
                 12: [2, 3, 5, 7, 11],
                 15: [2, 3, 5, 7, 11, 13],
                 23: [2, 3, 5, 7, 11, 13, 17, 19, 23]}

        for n in tests:
            assert eratosthenes(n) == tests[n]
