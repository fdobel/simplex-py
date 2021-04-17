import unittest
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_4
        self.tableau = tableau_4().get()

    def test_example4(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 33)
        self.assertEqual(sol['x_1'], 3)
        self.assertEqual(sol['x_2'], 12)

