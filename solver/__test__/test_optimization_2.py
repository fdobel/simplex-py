import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t2 = TableauBuilder()
        self.t2.add_constraint(constr_string_convert('2,5,>=,30'))
        self.t2.add_constraint(constr_string_convert('-3,5,>=,5'))
        self.t2.add_constraint(constr_string_convert('8,3,<=,85'))
        self.t2.add_constraint(constr_string_convert('-9,7,<=,42'))
        self.t2.set_objective(obj_string_convert('2,7,0'))

    def test_example2(self):
        result, sol = Optimization.max(self.t2.get())
        self.assertEqual(result, 104.15662650602411)
        self.assertEqual(sol['x1'], 5.650602)
        self.assertEqual(sol['x2'], 13.26506)
