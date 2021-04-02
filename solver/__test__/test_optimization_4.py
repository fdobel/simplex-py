import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_4
        self.tableau = tableau_4()

    def test_example4(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 33)
        self.assertEqual(sol['x1'], 3)
        self.assertEqual(sol['x2'], 12)

