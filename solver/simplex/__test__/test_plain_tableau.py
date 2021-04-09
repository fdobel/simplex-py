
import unittest

from solver.__test__.factories import tableau_1
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        self.tableau = tableau_1().get(optim="max")  # PlainTableau(, [2.0, 1.0])

    def test_objective(self):
        var_names, coeffs = self.tableau.objective_function

        self.assertEqual(var_names, ['x_1', 'x_2', '_s_1', '_s_2', '_a_1'])
        self.assertEqual(list(coeffs), [-5., -10., 0., 0., 1000.])

    def test_model_vars(self):
        self.assertEqual(self.tableau.model_vars, 2)

    def test_variable_count(self):
        self.assertEqual(self.tableau.variable_count, 5)

    def test_intermediate_solutino(self):
        sol = self.tableau.intermediate_solution()
        self.assertEqual(sol, VariableValues(["_a_1", "_s_2"], [10, 20]))
        self.assertEqual(str(sol), "_a_1:10.0;_s_2:20.0")

    def test_str(self):
        self.assertEqual(
            str(self.tableau),
            "[x_1, x_2, _s_1, _s_2, _a_1]\n"
            "[-2.0, 1.0, 1.0, 0.0, -1.0, -10.0]\n"
            "[1.0, 1.0, 0.0, 1.0, 0.0, 20.0]\n"
            "[-5.0, -10.0, 0.0, 0.0, 1000.0, 0.0]"
        )

    def test_base_var_indices(self):
        self.assertEqual(self.tableau.base_var_indices, [4, 3])