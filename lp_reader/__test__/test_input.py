
import unittest


from ..read import read

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def test(self):
        self.program = read('lp_reader/__test__/program1.lp')

        self.assertEqual(self.program[0], "obj 0 0 0 1 2")
        self.assertEqual(self.program[1], ["constraint 1 2 3 4 5 6"])

    def test_error(self):
        with self.assertRaises(AssertionError):
            self.program = read("lp_reader/__test__/error_program.lp")


    def test_error_var_count(self):
        with self.assertRaises(AssertionError):
            self.program = read("lp_reader/__test__/error_program_2.lp")