
import unittest

from solver.helper.table_wrapper import TableauWithObjective
import numpy as np


class Test(unittest.TestCase):

    def setUp(self):
        self.tw = TableauWithObjective(np.array([1., 2.]), np.array([[1., 0.], [0., 1.]]), np.array([3.2, 2.7]))

    def test_str(self):
        res = list(self.tw.full_table)
        self.assertEqual(list(res[0]), list(np.array([1, 2, 0])))
        self.assertEqual(list(res[1]), list(np.array([1, 0, 3.2])))
        self.assertEqual(list(res[2]), list(np.array([0, 1, 2.7])))