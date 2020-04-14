import unittest

from bb.model.constraint import SmallerThanConstraint, GreaterThanConstraint, IntegerConstraint
from bb.model.model import Model
from bb.model_to_tableau import model_to_tableau
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableau import TableauBuilder

from solver.optim import Optimization
import numpy as np
import numpy.testing as npt

class Test(unittest.TestCase):

    def setUp(self):
        constraints = []

        constraints.append(SmallerThanConstraint([2, 1], 4))
        constraints.append(SmallerThanConstraint([1, 2], 3))
        constraints.append(GreaterThanConstraint([1, 0], 0))
        constraints.append(GreaterThanConstraint([0, 1], 0))
        constraints.append(IntegerConstraint("x1"))
        constraints.append(IntegerConstraint("x2"))

        objective = [1, 1]
        self.m = Model(objective, constraints)

    def test_example1(self):
        from bb.optim import Optimization

        Optimization(self.m).branch_and_bound()

