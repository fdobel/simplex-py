import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t1 = TableauBuilder()
        self.t1.add_constraint(constr_string_convert('2,-1,>=,10'))
        self.t1.add_constraint(constr_string_convert('1,1,<=,20'))
        self.t1.set_objective(obj_string_convert('5,10,0'))

    def test_example1(self):
        result, sol = Optimization.min(self.t1.get())
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)
