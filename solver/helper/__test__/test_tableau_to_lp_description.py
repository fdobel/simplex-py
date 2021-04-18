import unittest

from solver.helper.tableau_to_description import to_lp_description

from solver.helper.tableaus.read_from_files import builder_from_file


class Test(unittest.TestCase):

    def test(self):
        self.tableau = builder_from_file("__test__/program1.lp").get()
        obj, constraints, slack_vars, art_vars = to_lp_description(self.tableau)
        self.assertEqual(str(constraints[0]), "2.00*x_1 + -1.00*x_2 + -1.00*_s_1 + 0.00*_s_2 + 1.00*_a_1 <= 10.00")
        self.assertEqual(str(constraints[1]), "1.00*x_1 + 1.00*x_2 + 0.00*_s_1 + 1.00*_s_2 + 0.00*_a_1 <= 20.00")
        self.assertEqual(str(obj), "obj -5.00*x_1 + -10.00*x_2 + 0.00*_s_1 + 0.00*_s_2 + 1000.00*_a_1")
        self.assertEqual(slack_vars, { '_s_1', '_s_2' })
        self.assertEqual(art_vars, {'_a_1'})

    def test_program_2(self):
        self.tableau = builder_from_file("__test__/program2.lp").get()
        obj, constraints, slack_vars, artificial_var = to_lp_description(self.tableau)
        self.assertEqual(
            str(constraints[0]),
            "2.00*x_1 + 5.00*x_2 + -1.00*_s_1 + 0.00*_s_2 + 0.00*_s_3 + 0.00*_s_4 + 1.00*_a_1 + 0.00*_a_2 <= 30.00"
        )
        self.assertEqual(
            str(constraints[1]),
            "-3.00*x_1 + 5.00*x_2 + 0.00*_s_1 + -1.00*_s_2 + 0.00*_s_3 + 0.00*_s_4 + 0.00*_a_1 + 1.00*_a_2 <= 5.00"
        )
        self.assertEqual(
            str(constraints[2]),
            "8.00*x_1 + 3.00*x_2 + 0.00*_s_1 + 0.00*_s_2 + 1.00*_s_3 + 0.00*_s_4 + 0.00*_a_1 + 0.00*_a_2 <= 85.00"
        )
        self.assertEqual(
            str(constraints[3]),
            "-9.00*x_1 + 7.00*x_2 + 0.00*_s_1 + 0.00*_s_2 + 0.00*_s_3 + 1.00*_s_4 + 0.00*_a_1 + 0.00*_a_2 <= 42.00"
        )
        self.assertEqual(
            str(obj),
            "obj -2.00*x_1 + -7.00*x_2 + 0.00*_s_1 + 0.00*_s_2 + 0.00*_s_3 + 0.00*_s_4 + 1000.00*_a_1 + 1000.00*_a_2")
        self.assertEqual(slack_vars, { '_s_1', '_s_2', '_s_3', '_s_4' })
        self.assertEqual(artificial_var, { '_a_1', '_a_2' })
