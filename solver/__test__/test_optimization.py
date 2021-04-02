import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_1
        self.tableau = tableau_1()

    def test_example1(self):
        result, sol = Optimization.min(self.tableau)
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)
