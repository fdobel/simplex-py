import unittest

from solver.helper.constraint_description import LessEqualThan, GreaterEqualThan
from solver.helper.tableaus import TableauBuilder

from solver.pivoting.pivot import find_pivot


class Test(unittest.TestCase):

    def setUp(self):
        tb = TableauBuilder()
        self.tableau = tb.add_constraint(GreaterEqualThan([2, -1], 10))\
            .add_constraint(LessEqualThan([1, 1], 20))\
            .set_objective([5, 10, 0]).get()

    def test_pivot_step_1(self):
        self.assertEqual([1, 1], find_pivot(self.tableau.table))
