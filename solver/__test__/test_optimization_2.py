import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t1 = TableauBuilder()

        self.t1.add_constraint([2, 1, 4])
        self.t1.add_constraint([1, 2, 3])
        #self.t1.add_constraint([-1, 0, 0])
        #self.t1.add_constraint([0, -1, 0])
        # self.t1.add_constraint([-1, 0, -2])
        self.t1.set_objective([1, 1, 0])
        # [-1.  0.  0.  0.  0.  0.  1.  0.  0. - 2.]

    def test_example1(self):
        self.t1.add_constraint([-1, 0, -2])

        r = self.t1.get()
        result, sol = Optimization.max(r)
        # print(Optimization.max(r, 'table'))
        self.assertEqual(result, 2.3333333333333335)
        self.assertEqual(sol['x1'], 1.666667)
        self.assertEqual(sol['x2'], 0.666667)

    def test_example2(self):
        result, sol = Optimization.max(self.t1.get())
        self.assertEqual(result, 2.3333333333333335)
        self.assertEqual(sol['x1'], 1.666667)
        self.assertEqual(sol['x2'], 0.666667)

    def test_example3(self):
        self.t1.add_greater_than([1, 0, 2])
        result, sol = Optimization.max(self.t1.get())
        self.assertEqual(result, 2.0)
        self.assertEqual(sol['x1'], 2.0)
        self.assertEqual(sol['x2'], 0.0)

