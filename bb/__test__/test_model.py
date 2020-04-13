import unittest

from bb.model.constraint import SmallerThanConstraint, GreaterThanConstraint, IntegerConstraint
from bb.model.model import Model
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        constraints = []

        constraints.append(SmallerThanConstraint([2, 1], 4))
        constraints.append(SmallerThanConstraint([1, 2], 3))
        constraints.append(GreaterThanConstraint([1, 0], 0))
        constraints.append(GreaterThanConstraint([0, 1], 0))
        constraints.append(IntegerConstraint("x1"))
        constraints.append(IntegerConstraint("x2"))

        objective = [1, 2]
        self.m = Model(objective, constraints)


    def test_example1(self):
        self.assertEqual(str(self.m), "----[1, 2]\n[2, 1]<=4\n[1, 2]<=3\n[1, 0]>=0\n[0, 1]>=0\nI: x1\nI: x2\n----")