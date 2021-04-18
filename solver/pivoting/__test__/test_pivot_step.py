import unittest

from constraint_description import LessEqualThan, GreaterEqualThan
from solver.helper.tableaus import TableauBuilder

from solver.pivoting.pivot import find_pivot


class Test(unittest.TestCase):

    def setUp(self):
        self.t2 = TableauBuilder()
        self.tableau = self.t2.add_constraint(GreaterEqualThan([2,  5], 30)).\
            add_constraint(GreaterEqualThan([-3,  5], 5)).\
            add_constraint(LessEqualThan([8, 3], 85)).\
            add_constraint(LessEqualThan([-9, 7], 42)).\
            set_objective([2, 7]).get()
    """
    @unittest.skip
    def test_pivot_step_0(self):
        self.assertEqual([1, 1], find_pivot_from_row(self.tableau.table))
    """
    def test_pivot_step_1(self):
        self.assertEqual([1, 1], find_pivot(self.tableau.table))
