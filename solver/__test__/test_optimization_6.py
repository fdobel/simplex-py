import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_6
        self.tb = tableau_6()

    def test_output(self):
        table = self.tb.get()

        rows = list(table.table)
        self.assertEqual(list(rows[0]), [4.0, 4.0, 1.0, 0.0, 0.0, 6.0])
        self.assertEqual(list(rows[1]), [-1.0, -3.0, 0.0, 1.0, -1.0, -2.0])

    def test_example4(self):
        result, sol = Optimization.max(self.tb.get())
        self.assertEqual(result, 7.499999999999999)
        self.assertEqual(sol['x1'], 0)
        self.assertEqual(sol['x2'], 1.5)

    def test_unbound_objective(self):
        result, sol = Optimization.min(self.tb.get())
        # print(result, sol)
        self.assertEqual(sol, {'x1': 1.25, 'x2': 0.25})



