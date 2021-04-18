import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from solver.helper.tableaus.read_from_files import builder_from_file
        self.tableau = builder_from_file("__test__/program4.lp").get()

    def test_example4(self):
        result, sol = Optimization.max(self.tableau)
        self.assertEqual(result, 33)
        self.assertEqual(sol['x_1'], 3)
        self.assertEqual(sol['x_2'], 12)

