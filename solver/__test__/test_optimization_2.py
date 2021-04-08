import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_2
        self.tableau = tableau_2().get()

    def test_example2(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 104.15662650602411)
        self.assertEqual(sol['x_1'], 5.650602)
        self.assertEqual(sol['x_2'], 13.26506)

    def test_iteration(self):
        res = [i for i in
               Optimization.run_simplex_iteratively(
                   self.tableau.table, var_names=self.tableau.var_names, initial_base_indices=[6, 7, 4, 5]
               )]

        self.assertEqual(len(res), 6)
        self.assertEqual(res[0], VariableValues(["_a_1", "_a_2","_s_3","_s_4"], [30.0, 5.0, 85.0, 42.0]))
        self.assertEqual(res[1], VariableValues(["_a_1", "x_2", "_s_3", "_s_4"], [25.0, 1.0, 82.0, 35.0]))
        self.assertEqual(res[2], VariableValues(["x_1", "x_2", "_s_3", "_s_4"], [5.0, 4.0, 33.0, 58.99999999999999]))
        self.assertEqual(res[3], VariableValues(["x_1", "x_2", "_s_1", "_s_4"],
                                                [8.36734693877551, 6.020408163265307, 16.836734693877553, 75.16326530612244]))
        self.assertEqual(res[4], VariableValues(["x_1", "x_2", "_s_1", "_s_2"],
                                                [5.6506024096385525, 13.265060240963855, 47.626506024096386, 44.373493975903614]))
        self.assertEqual(res[5], VariableValues(["x_1", "x_2", "_s_1", "_s_2"],
                                                [5.650602409638553, 13.265060240963857, 47.626506024096386, 44.373493975903614]))


