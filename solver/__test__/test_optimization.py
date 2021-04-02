import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_1
        self.tableau_builder = tableau_1()

    def test_example1(self):
        tableau = self.tableau_builder.get(enable_artif_vars=False)
        print(tableau)
        result, sol = Optimization.min(tableau)
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)

    def test_example_2(self):
        tableau = self.tableau_builder.get(enable_artif_vars=True)
        print(tableau)
        result, sol = Optimization.min(tableau)
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)