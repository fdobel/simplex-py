import unittest

from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.simplex.plain_tableau import PlainTableau
from solver.helper.tableaus.tableau_builder import TableauBuilder


class Test(unittest.TestCase):

    def setUp(self):
        self.tb = TableauBuilder()

    def test_empty(self):
        with self.assertRaises(TypeError):
            self.tb.get()

    def test_single_constraint(self):
        self.tb.add_constraint(constr_string_convert('2,5,>=,30'))
        with self.assertRaises(TypeError):
            self.tb.get()

    def test_single_constraint_and_objective(self):
        self.tb.add_constraint(constr_string_convert('2,5,>=,30'))
        self.tb.set_objective(obj_string_convert('5,10,0'))
        res = self.tb.get()
        self.assertIsInstance(res, PlainTableau)

    def test_single_constraint_and_objective_result(self):
        self.tb.add_constraint(constr_string_convert('2,5,>=,30'))
        self.tb.set_objective(obj_string_convert('5,10,0'))
        res = self.tb.get()
        res_list = list(res.table)
        self.assertEqual(list(res_list[0]), [ -2.,  -5.,   1.,  -1,  -30.])
        self.assertEqual(list(res_list[1]), [ -5., -10.,   0.,   1000, 0.])
