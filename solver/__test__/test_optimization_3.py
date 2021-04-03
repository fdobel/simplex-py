import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_3
        self.tableau = tableau_3()

    def test_example3(self):
        result, sol = Optimization.max(self.tableau.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x1'], 45)
        self.assertEqual(sol['x2'], 6.25)

    def test_example_with_bigm(self):
        t = self.tableau.get(enable_artif_vars=True)
        print(t)
        result, sol = Optimization.max(t)
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x1'], 45)
        self.assertEqual(sol['x2'], 6.25)
