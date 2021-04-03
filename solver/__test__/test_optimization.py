import unittest

from solver.optim import Optimization
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_1
        self.tableau_builder = tableau_1()

    def test_example1(self):
        tableau = self.tableau_builder.get(enable_artif_vars=False)
        result, sol = Optimization.min(tableau)
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)

    def test_example_2(self):
        tableau = self.tableau_builder.get(enable_artif_vars=True)
        result, sol = Optimization.min(tableau)
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)

    def test_step_1(self):
        t = self.tableau_builder.get()
        sol = t.intermediate_solution()
        self.assertEqual(sol, VariableValues(["_a_1", "_s_2"], [10, 20]))
