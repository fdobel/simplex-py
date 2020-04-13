import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t1 = TableauBuilder()
        self.t1.add_constraint(constr_string_convert('2,-1,>=,10'))
        self.t1.add_constraint(constr_string_convert('1,1,<=,20'))
        self.t1.set_objective(obj_string_convert('5,10,0'))

        self.t2 = TableauBuilder()
        self.t2.add_constraint(constr_string_convert('2,5,>=,30'))
        self.t2.add_constraint(constr_string_convert('-3,5,>=,5'))
        self.t2.add_constraint(constr_string_convert('8,3,<=,85'))
        self.t2.add_constraint(constr_string_convert('-9,7,<=,42'))
        self.t2.set_objective(obj_string_convert('2,7,0'))

        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('50,24,<=,2400'))
        self.t3.add_constraint(constr_string_convert('30,33,<=,2100'))
        self.t3.add_constraint(constr_string_convert('1,0,>=,45'))
        self.t3.add_constraint(constr_string_convert('0,1,>=,5'))
        self.t3.set_objective(obj_string_convert('1,1,0'))

    def test_example1(self):
        result, sol = Optimization.min(self.t1.get())
        self.assertEqual(result, 25.0)
        self.assertEqual(sol['x1'], 5.0)
        self.assertEqual(sol['x2'], 0)

    def test_example2(self):
        result, sol = Optimization.max(self.t2.get())
        self.assertEqual(result, 104.15662650602411)
        self.assertEqual(sol['x1'], 5.650602)
        self.assertEqual(sol['x2'], 13.26506)

    def test_example3(self):
        result, sol = Optimization.max(self.t3.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x1'], 45)
        self.assertEqual(sol['x2'], 6.25)

