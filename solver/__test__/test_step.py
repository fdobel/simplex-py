import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder, PlainTableau

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('2,1,<=,18'))
        self.t3.add_constraint(constr_string_convert('2,3,<=,42'))
        self.t3.add_constraint(constr_string_convert('3,1,<=,24'))
        self.t3.set_objective(obj_string_convert('3,2,0'))


    @unittest.skip
    def test_variable_name(self):
        t = self.t3.get()
        res = PlainTableau(t.table).get_variable_names()
        self.assertEqual(['x1', 'x2'], res)

    def test_example4(self):
        t = self.t3.get()
        print(t.table)
        res = PlainTableau(t.table).collect_result()
        self.assertEqual({ 'x1': 0, 'x2': 0}, res)

    def test_step(self):
        t = self.t3.get()
        t2 = Optimization.do_simplex_step2(t.table)
        res = PlainTableau(t2).collect_result()
        self.assertEqual({ 'x1': 8.0, 'x2': 0}, res)

    def test_step_2(self):
        t = self.t3.get()
        t2 = Optimization.do_simplex_step2(t.table)
        t3 = Optimization.do_simplex_step2(t2)
        res = PlainTableau(t3).collect_result()
        self.assertEqual({ 'x1': 6.0, 'x2': 5.999999999999999}, res)

    def test_step_3(self):
        t = self.t3.get()
        t2 = Optimization.do_simplex_step2(t.table)
        t3 = Optimization.do_simplex_step2(t2)
        t4 = Optimization.do_simplex_step2(t3)
        res = PlainTableau(t4).collect_result()
        self.assertEqual({ 'x1': 2.9999999999999996, 'x2': 12.0}, res)

    def test_step_4(self):
        t = self.t3.get()
        t2 = Optimization.do_simplex_step2(t.table)
        t3 = Optimization.do_simplex_step2(t2)
        t4 = Optimization.do_simplex_step2(t3)
        t5 = Optimization.do_simplex_step2(t4)
        res = PlainTableau(t5).collect_result()
        self.assertEqual({ 'x1': 2.9999999999999996, 'x2': 12.0}, res)
