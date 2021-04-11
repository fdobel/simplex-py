import unittest

from solver.__test__.factories import tableau_1
from solver.pivoting.equivalent_conversion.extract_from_tableau import \
    constraints_from, objective_from, variable_names_from, \
    slack_variables_from, artificial_variables_from


class Test(unittest.TestCase):
    def setUp(self):
        self.tableau = tableau_1().get(optim="max")

    def test_result(self):
        res = constraints_from(tableau=self.tableau)

        self.assertEqual(len(res), 2)
        self.assertEqual("2.00*x_0 + -1.00*x_1 + -1.00*x_2 + 0.00*x_3 + 1.00*x_4 <= 10.00", str(res[0]))
        self.assertEqual("1.00*x_0 + 1.00*x_1 + 0.00*x_2 + 1.00*x_3 + 0.00*x_4 <= 20.00", str(res[1]))

    def test_objective(self):
        self.assertEqual(
            "min -5.00*x_0 + -10.00*x_1 + 0.00*x_2 + 0.00*x_3 + 1000.00*x_4",
            str(objective_from(tableau=self.tableau))
        )

    def test_var_names(self):
        self.assertEqual(
            variable_names_from(self.tableau),
            ['x_1', 'x_2', '_s_1', '_s_2', '_a_1']
        )

    def test_get_slack_vars(self):
        self.assertEqual(
            slack_variables_from(self.tableau),
            ['_s_1', '_s_2']
        )

    def test_get_artificial_vars(self):
        self.assertEqual(
            artificial_variables_from(self.tableau),
            ['_a_1']
        )

