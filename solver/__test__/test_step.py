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
        # self.t3.add_constraint(constr_string_convert('1,0,>=,0'))
        # self.t3.add_constraint(constr_string_convert('0,1,>=,0'))
        self.t3.set_objective(obj_string_convert('3,2,0'))


    def test_variable_name(self):
        t = self.t3.get()
        # print(t)
        # print(t.table)
        res = PlainTableau(t.table).get_variable_names()
        # print(res)
        self.assertEqual(['x1', 'x2'], res)

    def test_example4(self):
        t = self.t3.get()
        # print(t)
        # print(t.table)
        res = PlainTableau(t.table).collect_result()
        # print(res)
        self.assertEqual({ 'x1': 0, 'x2': 0}, res)
        # table2 = Optimization.do_simplex_step2(t.table)
        # print(table2)

