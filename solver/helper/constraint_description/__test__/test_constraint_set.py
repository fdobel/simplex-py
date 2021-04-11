import unittest

from solver.helper.constraint_description.constraint_set import ConstraintSet
from .. import GreaterEqualThan, LessEqualThan


class Test(unittest.TestCase):

    def setUp(self):
        self.cs = ConstraintSet([
            GreaterEqualThan([0, 1, 2], 42),
            LessEqualThan([0, 1, 2], 42)
        ])

        self.cs2 = ConstraintSet([
            GreaterEqualThan([0, 1, 2], 42, var_names=["t1", "t2", "t3"]),
            LessEqualThan([0, 1, 2], 42, var_names=["x1", "x2", "t3"])
        ])\
            .define_var_type("t1", "model")\
            .define_var_type("t2", "slack")\
            .define_var_type("t3", "slack") \
            .define_var_type("x1", "artificial") \
            .define_var_type("x2", "artificial")

    def test_constraint_set(self):
        self.assertEqual(self.cs.__len__(), 2)

    def test_str(self):
        self.assertEqual(
            str(self.cs),
            "0.00*x_0 + 1.00*x_1 + 2.00*x_2 >= 42.00\n"
            "0.00*x_0 + 1.00*x_1 + 2.00*x_2 <= 42.00"
        )

    def test_unique_vars(self):
        self.assertEqual(self.cs.unique_vars(), {'x_0', 'x_1', 'x_2'})

    def test_unique_vars_2(self):
        self.assertEqual(self.cs2.unique_vars(), {'t1', 't2', 't3', 'x1', 'x2'})

    def test_model_vars(self):
        self.assertEqual(self.cs2.model_variables(), {"t1"})

    def test_slack_vars(self):
        self.assertEqual(self.cs2.slack_variables(), {"t2", "t3"})

    def test_artificial_vars(self):
        self.assertEqual(self.cs2.artificial_variables(), {"x1", "x2"})
