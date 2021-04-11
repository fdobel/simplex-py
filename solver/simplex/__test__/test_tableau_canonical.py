
import unittest

from solver.__test__.factories import tableau_1, tableau_2, tableau_4
from solver.optim import Optimization
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.solution import VariableValues


class Test(unittest.TestCase):

    def test_canonical(self):
        self.tableau = tableau_1().get(optim="max")
        self.assertEqual(self.tableau.is_canonical(), False)

    def test_make_canonical(self):
        self.tableau = tableau_1().get(optim="max")
        t = Optimization._to_canonical(self.tableau.table, self.tableau.base_var_indices)
        tbl = PlainTableau(t, self.tableau.var_names, self.tableau._model_vars, self.tableau.base_var_indices)
        self.assertEqual(tbl.is_canonical(), True)

    def test_canonical_2(self):
        self.tableau = tableau_2().get(optim="max")
        self.assertEqual(self.tableau.is_canonical(), False)

    def test_make_canonical_2(self):
        self.tableau = tableau_2().get(optim="max")
        t = Optimization._to_canonical(self.tableau.table, self.tableau.base_var_indices)
        tbl = PlainTableau(t, self.tableau.var_names, self.tableau._model_vars, self.tableau.base_var_indices)
        self.assertEqual(tbl.is_canonical(), True)

    def test_canonical_tableau_4(self):
        self.tableau = tableau_4().get(optim="max")
        self.assertEqual(self.tableau.is_canonical(), True)
