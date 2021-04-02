import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_3
        self.tableau = tableau_3()

    def test_example3(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x1'], 45)
        self.assertEqual(sol['x2'], 6.25)

