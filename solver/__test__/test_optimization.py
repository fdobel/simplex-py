import unittest

from solver.optim import Optimization
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_1
        self.tableau_builder = tableau_1()

    def test_example_min(self):
        tableau = self.tableau_builder.get(optim="max")
        result, sol = Optimization.max(tableau)
        self.assertEqual(result, 150.0)
        self.assertEqual(sol['x_1'], 10.0)
        self.assertEqual(sol['x_2'], 10)

    def test_example_3(self):
        tableau = self.tableau_builder.get(optim="min")
        result, sol = Optimization.max(tableau)
        self.assertEqual(result, -25.0)
        self.assertEqual(sol['x_1'], 5.0)
        self.assertEqual(sol['x_2'], 0)

    def test_step_1(self):
        t = self.tableau_builder.get()
        sol = t.intermediate_solution()
        self.assertEqual(sol, VariableValues(["_a_1", "_s_2"], [10, 20]))
