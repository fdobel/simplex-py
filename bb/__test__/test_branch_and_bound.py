
import unittest

from constraint_description import GreaterEqualThan, LessEqualThan, ConstraintSet, Min, Max
from constraint_description.variable_constraint import IsNaturalNumber
from solver.optim import Optimization
from solver.tableau_from_constraint_description import transform


class Test(unittest.TestCase):
    def setUp(self):
        self.cs = ConstraintSet([
            LessEqualThan([0.73, 1, 2], 42),
            LessEqualThan([0, 1, 0], 55)
        ], variable_constraints=[IsNaturalNumber("x_1")])\
            .define_var_type('x_1', 'model') \
            .define_var_type('x_2', 'model') \
            .define_var_type('x_3', 'model')
        self.optim_function = Max([2.11, 2, 2])

    def test(self):
        from ..on_constraint_set import compute
        # self.tableau = transform(self.cs, self.optim_function)
        # result, sol = Optimization.max(self.tableau)
        # self.assertEqual(result, 121.39726027397262)
        # self.assertEqual(sol, {'x_1': 57.534247, 'x_2': 0, 'x_3': 0})
        self.assertEqual(compute(self.cs, self.optim_function), 41)
