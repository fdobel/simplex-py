import unittest

from solver.helper.tableaus.read_from_files import builder_from_file
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.tableau = builder_from_file("__test__/program3.lp")

    def test_min(self):
        result, sol = Optimization.max(self.tableau.get(optim="min"))
        self.assertEqual(result, -50)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 5)

    def test_example4(self):
        result, sol = Optimization.max(self.tableau.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 6.25)

