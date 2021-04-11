import unittest

from ..objective import Min
from .. import GreaterEqualThan, LessEqualThan


class Test(unittest.TestCase):

    def setUp(self):
        self._c1 = GreaterEqualThan([0, 1, 2], 42)
        self._c2 = LessEqualThan([0, 1, 2], 42)

    def test_greater_equal_than(self):
        self.assertEqual(
            str(self._c1),
            "0.00*x_0 + 1.00*x_1 + 2.00*x_2 >= 42.00"
        )

    def test_less_equal_than(self):
        self.assertEqual(
            str(self._c2),
            "0.00*x_0 + 1.00*x_1 + 2.00*x_2 <= 42.00"
        )

    def test_objective(self):
        self.assertEqual(
            str(Min([1, 2, 3])),
            "min 1.00*x_0 + 2.00*x_1 + 3.00*x_2"
        )


