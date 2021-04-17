import unittest
from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_5
        self.tb = tableau_5()

    def test_output(self):
        table = self.tb.get()

        rows = list(table.table)
        self.assertEqual(list(rows[0]), [4.0, 4.0, 1.0, 0.0, 0.0, 6.0])
        self.assertEqual(list(rows[1]), [1.0, 3.0, 0.0, -1.0, 1.0, 2.0])

    def test_example4(self):
        result, sol = Optimization.max(self.tb.get())
        self.assertAlmostEqual(result, 7.499999999999999, places=7)
        self.assertEqual(sol['x_1'], 0)
        self.assertEqual(sol['x_2'], 1.5)

    def test_unbound_objective(self):
        result, sol = Optimization.max(self.tb.get(optim="min"))
        self.assertAlmostEqual(result, -2.5, places=7)
        self.assertEqual(sol, {'x_1': 1.25, 'x_2': 0.25})



