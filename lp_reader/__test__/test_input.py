
import unittest


from ..read import read

class Test(unittest.TestCase):

    def test(self):
        self.program = read('lp_reader/__test__/program1.lp')

        self.assertEqual(self.program[0], [0, 0, 0, 1, 2])
        self.assertEqual(self.program[1], [([1, 2, 3, 4, 5], '<=', 6)])

    def test_program_2(self):
        self.program = read('lp_reader/__test__/program2.lp')

        self.assertEqual(self.program[0], [5, 10])
        self.assertEqual(self.program[1], [([2, -1], '>=', 10), ([1, 1], '<=', 20)])

    def test_program_3(self):
        self.program = read('lp_reader/__test__/program3.lp')

        self.assertEqual(self.program[0], [2, 7])
        self.assertEqual(self.program[1],
                         [
                             ([2, 5], '>=', 30),
                             ([-3, 5], '>=', 5),
                             ([8, 3], '<=', 85),
                             ([-9, 7], '<=', 42)
                         ])

    def test_error(self):
        with self.assertRaises(AssertionError):
            self.program = read("lp_reader/__test__/error_program.lp")

    def test_error_var_count(self):
        with self.assertRaises(AssertionError):
            self.program = read("lp_reader/__test__/error_program_2.lp")