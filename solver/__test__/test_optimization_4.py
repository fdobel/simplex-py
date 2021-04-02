import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('2,1,<=,18'))
        self.t3.add_constraint(constr_string_convert('2,3,<=,42'))
        self.t3.add_constraint(constr_string_convert('3,1,<=,24'))
        # self.t3.add_constraint(constr_string_convert('1,0,>=,0'))
        # self.t3.add_constraint(constr_string_convert('0,1,>=,0'))
        self.t3.set_objective(obj_string_convert('3,2,0'))

    def test_example4(self):
        result, sol = Optimization.max(self.t3.get())
        self.assertEqual(result, 33)
        self.assertEqual(sol['x1'], 3)
        self.assertEqual(sol['x2'], 12)

