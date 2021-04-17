import unittest

from solver.helper.constraint_description import LessEqualThan
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(LessEqualThan([2, 1], 18)).\
            add_constraint(LessEqualThan([2, 3], 42)). \
            add_constraint(LessEqualThan([3, 1], 24)).\
            set_objective([3, 2, 0])

    def test_example4(self):
        t = self.t3.get()
        self.assertEqual(str(t.intermediate_solution()), "_s_1:18.0;_s_2:42.0;_s_3:24.0")


