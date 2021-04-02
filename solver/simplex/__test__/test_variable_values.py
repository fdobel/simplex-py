
import unittest

from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def setUp(self):
        self.v = VariableValues(["x1", "y1"], [1.0, 2.0])

    def test_str(self):
        self.assertEqual("x1:1.0;y1:2.0", self.v.__str__())
