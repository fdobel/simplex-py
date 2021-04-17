import unittest

from solver.helper.constraint_description import GreaterEqualThan
from solver.simplex.plain_tableau import PlainTableau
from solver.helper.tableaus.tableau_builder import TableauBuilder


class Test(unittest.TestCase):

    def setUp(self):
        self.tb = TableauBuilder()

    def test_empty(self):
        with self.assertRaises(TypeError):
            self.tb.get()

    def test_single_constraint(self):
        self.tb.add_constraint(GreaterEqualThan([2, 5], 30))
        with self.assertRaises(TypeError):
            self.tb.get()

    def test_single_constraint_and_objective(self):
        self.tb.add_constraint(GreaterEqualThan([2, 5], 30))
        self.tb.set_objective([5, 10, 0])
        res = self.tb.get()
        self.assertIsInstance(res, PlainTableau)

    def test_single_constraint_and_objective_result(self):
        self.tb.add_constraint(GreaterEqualThan([2, 5], 30))
        self.tb.set_objective([5, 10, 0])
        res = self.tb.get()
        res_list = list(res.table)
        self.assertEqual(list(res_list[0]), [ 2.,  5.,   -1.,  1,  30.])
        self.assertEqual(list(res_list[1]), [ -5., -10.,   0.,   1000, 0.])
