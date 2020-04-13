
from solver.helper.tableau import PlainTableau
from solver.pivoting.pivot import find_pivot_from_row, find_pivot
from solver.pivoting.table_functions import is_not_final_tableau_r, is_not_final_tableau

import numpy as np


def _round_result(val):
    for k, v in val.items():
        val[k] = round(v, 6)
    return val


def compute_new_tableau(piv_pos, old_tableau):
    piv_row_idx, piv_col_idx = piv_pos

    lr = len(old_tableau[:, 0])
    lc = len(old_tableau[0, :])
    new_tableau = np.zeros((lr, lc))
    pivot_row = old_tableau[piv_row_idx, :]

    piv_element = old_tableau[piv_row_idx, piv_col_idx]

    if piv_element != 0:

        r = 1 / piv_element * pivot_row

        # update non-pivot rows
        for i in range(lr):
            if i == piv_row_idx:
                continue

            new_tableau[i, :] = old_tableau[i, :] - r * old_tableau[i, piv_col_idx]

        # pivot row update
        new_tableau[piv_row_idx, :] = r
        return new_tableau
    else:
        print('Cannot pivot on this element.')


class Optimization:

    def __init__(self):
        pass

    @staticmethod
    def run_simplex(table):
        while is_not_final_tableau_r(table):
            piv_pos = find_pivot_from_row(table)
            table = compute_new_tableau(piv_pos, table)
        while is_not_final_tableau(table):
            piv_pos = find_pivot(table)
            table = compute_new_tableau(piv_pos, table)
        return table

    def run(self, tableau: PlainTableau):

        final_table = self.run_simplex(tableau.table)

        val = PlainTableau(final_table).collect_result()

        return val, final_table

    @classmethod
    def max(cls, table: PlainTableau, output='summary'):
        val, table = Optimization().run(table)

        if output == 'table':
            return table
        else:
            max_ = table[-1, -1]
            return max_, _round_result(val)

    @classmethod
    def min(cls, tableau: PlainTableau, output='summary'):
        val, table = Optimization().run(tableau.convert_min())

        if output == 'table':
            return table
        else:
            min_ = table[-1, -1] * -1
            return min_, _round_result(val)
