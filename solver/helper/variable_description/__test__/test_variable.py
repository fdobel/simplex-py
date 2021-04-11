import unittest

from solver.helper.variable_description.variable import ModelVariable, SlackVariable, ArtificialVariable


class Test(unittest.TestCase):

    def setUp(self):
        self.mv1 = ModelVariable("x_1")
        self.mv2 = ModelVariable("x_1")

        self.sv = SlackVariable("_s_1")
        self.av = ArtificialVariable("_a_1")

    def test_eq(self):
        self.assertEqual(self.mv1, self.mv2)

    def test_eq_2(self):
        self.assertEqual(
            SlackVariable("x"),
            SlackVariable("x")
        )

    def test_neq(self):
        self.assertNotEqual(
            ModelVariable("x"),
            SlackVariable("x")
        )


