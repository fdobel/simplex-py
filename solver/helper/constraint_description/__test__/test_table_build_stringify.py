import unittest

from solver.helper.constraint_description.tableau_to_description import stringify


class Test(unittest.TestCase):

    def setUp(self):
        from solver.__test__.factories import tableau_1
        self.tableau = tableau_1()

    def test(self):
        res = stringify(self.tableau)
        self.assertEqual(str(res[0]), "-2.00*x_0 + 1.00*x_1 + 1.00*x_2 + 0.00*x_3 <= -10.00")
        self.assertEqual(str(res[1]), "1.00*x_0 + 1.00*x_1 + 0.00*x_2 + 1.00*x_3 <= 20.00")
        self.assertEqual(str(res[2]), "min -5.00*x_0 + -10.00*x_1 + 0.00*x_2 + 0.00*x_3")