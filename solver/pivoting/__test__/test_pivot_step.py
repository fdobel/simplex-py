import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.pivoting.pivot import find_pivot_from_row, find_pivot


class Test(unittest.TestCase):

    def setUp(self):
        self.t2 = TableauBuilder()
        self.tableau = self.t2.add_constraint(constr_string_convert('2,5,>=,30')).\
            add_constraint(constr_string_convert('-3,5,>=,5')).\
            add_constraint(constr_string_convert('8,3,<=,85')).\
            add_constraint(constr_string_convert('-9,7,<=,42')).\
            set_objective(obj_string_convert('2,7,0')).get()

    @unittest.skip
    def test_pivot_step_0(self):
        self.assertEqual([1, 1], find_pivot_from_row(self.tableau.table))

    def test_pivot_step_1(self):
        self.assertEqual([1, 1], find_pivot(self.tableau.table))
