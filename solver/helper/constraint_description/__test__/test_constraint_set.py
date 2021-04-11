import unittest

from solver.helper.constraint_description.constraint_set import ConstraintSet
from ..objective import Min
from .. import GreaterEqualThan, LessEqualThan


class Test(unittest.TestCase):

    def setUp(self):
        self._c1 = GreaterEqualThan([0, 1, 2], 42)
        self._c2 = LessEqualThan([0, 1, 2], 42)
        self.cs = ConstraintSet([self._c1, self._c2])

    def test_constraint_set(self):
        self.assertEqual(self.cs.__len__(), 2)

    def test_str(self):
        self.assertEqual(str(self.cs), "0.00*x_0 + 1.00*x_1 + 2.00*x_2 >= 42.00\n0.00*x_0 + 1.00*x_1 + 2.00*x_2 <= 42.00")

    def test_unique_vars(self):
        self.assertEqual(self.cs.unique_vars(), {'x_0', 'x_1', 'x_2'})


