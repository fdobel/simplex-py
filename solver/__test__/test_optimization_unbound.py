import unittest

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        from .factories import tableau_unbound
        self.tb = tableau_unbound()

    def test_output(self):
        table = self.tb.get()

        rows = list(table.table)
        self.assertEqual(list(rows[0]), [-1.0, -1.0, 1.0, 0.0])
        self.assertEqual(list(rows[1]), [-1.0, -1.0, 0.0, 0.0])

    def test_example4(self):
        result, sol = Optimization.max(self.tb.get(optim="max"))
        self.assertEqual(result, "unbounded")
        self.assertEqual(sol, {})

    def test_unbound_objective(self):
        result, sol = Optimization.max(self.tb.get(optim="min"))
        self.assertEqual(result, 0.0)
        self.assertEqual(sol, {'x_1': 0, 'x_2': 0})



