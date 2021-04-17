import unittest
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_3
        self.tableau = tableau_3()

    def test_min(self):
        result, sol = Optimization.max(self.tableau.get(optim="min"))
        self.assertEqual(result, -50)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 5)

        """
        tb.add_constraint(constr_string_convert('50,24,<=,2400')) \
            .add_constraint(constr_string_convert('30,33,<=,2100')) \
            .add_constraint(constr_string_convert('1,0,>=,45')) \
            .add_constraint(constr_string_convert('0,1,>=,5')) \
            .set_objective(obj_string_convert('1,1,0'))
        """

    def test_example4(self):
        result, sol = Optimization.max(self.tableau.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 6.25)

