import unittest

from constraint_description.variable_constraint import IsNaturalNumber
from ..objective import Min
from .. import GreaterEqualThan, LessEqualThan


class Test(unittest.TestCase):

    def setUp(self):
        self.vc = IsNaturalNumber("x_1")

    def test_is_natural_number(self):
        self.assertEqual(
            str(self.vc),
            "x_1 ∈ ℕ"
        )
