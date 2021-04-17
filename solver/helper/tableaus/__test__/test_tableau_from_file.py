import unittest

from solver.helper.tableaus.read_from_files import tableau_from_file


class Test(unittest.TestCase):

    def test_str(self):
        t = tableau_from_file("__test__/program_0.lp")
        self.assertEqual(
            str(t),
            "[x_1, x_2, x_3, x_4, x_5, _s_1]\n"
            "[1.0, 2.0, 3.0, 4.0, 5.0, 1.0, 6.0]\n"
            "[0.0, 0.0, 0.0, -1.0, -2.0, 0.0, 0.0]")
