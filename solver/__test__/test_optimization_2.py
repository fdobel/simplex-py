import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_2
        self.tableau = tableau_2().get()

    def test_example2(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 104.15662650602411)
        self.assertEqual(sol['x1'], 5.650602)
        self.assertEqual(sol['x2'], 13.26506)
