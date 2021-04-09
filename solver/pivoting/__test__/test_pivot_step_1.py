import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder
from solver.optim import Optimization

from solver.pivoting.pivot import find_pivot_from_row, find_pivot
from solver.pivoting.table_functions import is_not_final_tableau_r


class Test(unittest.TestCase):

    def setUp(self):
        tb = TableauBuilder()
        self.tableau = tb.add_constraint(constr_string_convert('2,-1,>=,10'))\
            .add_constraint(constr_string_convert('1,1,<=,20'))\
            .set_objective(obj_string_convert('5,10,0')).get()

    @unittest.skip
    def test_pivot_step_0(self):
        # print(self.tableau.table)
        self.assertEqual([0, 0], find_pivot_from_row(self.tableau.table))
        # next_table = Optimization.do_simplex_step(self.tableau.table)

    # @unittest.skip
    def test_pivot_step_1(self):
        self.assertEqual([1, 1], find_pivot(self.tableau.table))
