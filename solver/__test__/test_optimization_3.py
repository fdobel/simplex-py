import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('50,24,<=,2400'))
        self.t3.add_constraint(constr_string_convert('30,33,<=,2100'))
        self.t3.add_constraint(constr_string_convert('1,0,>=,45'))
        self.t3.add_constraint(constr_string_convert('0,1,>=,5'))
        self.t3.set_objective(obj_string_convert('1,1,0'))

    def test_example3(self):
        result, sol = Optimization.max(self.t3.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x1'], 45)
        self.assertEqual(sol['x2'], 6.25)

