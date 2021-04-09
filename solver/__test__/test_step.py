import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('2,1,<=,18'))
        self.t3.add_constraint(constr_string_convert('2,3,<=,42'))
        self.t3.add_constraint(constr_string_convert('3,1,<=,24'))
        self.t3.set_objective(obj_string_convert('3,2,0'))

        self.var_names = ['x_1', 'x_2', '_s_1', '_s_2', '_s_3']

    @unittest.skip
    def test_variable_name(self):
        t = self.t3.get()
        res = PlainTableau(t.table, model_vars=['x_1', 'x_2']).get_variable_names()
        self.assertEqual(['x1', 'x2'], res)

    def test_example4(self):
        t = self.t3.get()
        tbl = PlainTableau(t.table, var_names=self.var_names, model_vars=['x_1', 'x_2'], base_var_indices=[2, 3, 4])

        res = tbl.collect_result()
        # print(res)
        self.assertEqual(VariableValues.from_dict({ 'x_1': 0, 'x_2': 0}), res)

    def test_step(self):
        t = self.t3.get()
        # print(t)
        t2, pp = Optimization.do_simplex_step2(t.table)

        res = PlainTableau(t2, var_names=self.var_names, model_vars=['x_1', 'x_2'], base_var_indices=[0, 2, 3]).collect_result()
        self.assertEqual(VariableValues.from_dict({ 'x_1': 8.0, 'x_2': 0}), res)

    def test_step_2(self):
        t = self.t3.get()
        t2, pp = Optimization.do_simplex_step2(t.table)
        t3, pp = Optimization.do_simplex_step2(t2)

        res = PlainTableau(t3, var_names=self.var_names, model_vars=['x_1', 'x_2'], base_var_indices=[0, 1, 3]).collect_result()
        self.assertEqual(VariableValues.from_dict({ 'x_1': 6.0, 'x_2': 5.999999999999999}), res)

    def test_step_3(self):
        t = self.t3.get()
        t2, pp = Optimization.do_simplex_step2(t.table)
        t3, pp = Optimization.do_simplex_step2(t2)
        t4, pp = Optimization.do_simplex_step2(t3)

        res = PlainTableau(t4, var_names=self.var_names, model_vars=['x_1', 'x_2'], base_var_indices=[0,  1, 4]).collect_result()
        self.assertEqual(VariableValues.from_dict({ 'x_1': 2.9999999999999996, 'x_2': 12.0}), res)

    def test_step_4(self):
        t = self.t3.get()
        t2, pp = Optimization.do_simplex_step2(t.table)
        t3, pp = Optimization.do_simplex_step2(t2)
        t4, pp = Optimization.do_simplex_step2(t3)
        t5, pp = Optimization.do_simplex_step2(t4)

        res = PlainTableau(t5, var_names=self.var_names, model_vars=['x_1', 'x_2'], base_var_indices=[0, 1, 4]).collect_result()
        self.assertEqual(VariableValues.from_dict({ 'x_1': 2.9999999999999996, 'x_2': 12.0}), res)
