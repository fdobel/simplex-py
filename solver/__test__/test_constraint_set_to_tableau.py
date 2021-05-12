import unittest

from constraint_description import ConstraintSet, GreaterEqualThan, LessEqualThan, Min
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.cs = ConstraintSet([
            GreaterEqualThan([0, 1, 2], 42),
            LessEqualThan([0, 1, 2], 42)
        ])

    def test_a(self):
        from ..tableau_from_constraint_description import transform
        res = transform(self.cs, Min([1, 2, 3]))
        self.assertEqual(
            str(res),
            "[x_1, x_2, x_3, _s_1, _s_2, _a_1]\n"
            "[0.0, 1.0, 2.0, -1.0, 0.0, 1.0, 42.0]\n"
            "[0.0, 1.0, 2.0, 0.0, 1.0, 0.0, 42.0]\n"
            "[-1.0, -2.0, -3.0, 0.0, 0.0, 1000.0, 0.0]")
