import unittest

from solver.helper.tableaus.read_from_files import builder_from_file
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.tableau = builder_from_file("__test__/program3.lp")

    def test_max(self):
        result, sol = Optimization.max(self.tableau.get())
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 6.25)

    def test_example_with_bigm(self):
        t = self.tableau.get()
        # print(t)
        result, sol = Optimization.max(t)
        self.assertEqual(result, 51.25)
        self.assertEqual(sol['x_1'], 45)
        self.assertEqual(sol['x_2'], 6.25)
