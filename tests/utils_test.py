from ..primer.factor import eratosthenes

import unittest

class SieveofEratosthenesTest(unittest.TestCase):
    def test_prime_generation():
        tests = {2:      {2: 1},
                 17:     {17: 1},
                 384:    {2: 7, 3: 1},
                 29483:  {29483: 1},
                 583928: {2: 3, 47: 1, 1553: 1}}

        for n in tests:
            factors = dict(eratosthenes(n))
            self.assertEqual(factors, tests[n])

if __name__ == '__main__':
    unittest.main()
