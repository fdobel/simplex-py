
from solver.pivoting.pivot import find_pivot_from_row, find_pivot
from solver.pivoting.table_functions import is_not_final_tableau_r, is_not_final_tableau

import numpy as np

from solver.pivoting.unbounded_tableau_exception import UnboundedTableau
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.get_tableau_solution import table_solution_from_base_indices


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

    """
    @staticmethod
    def do_simplex_step(table):
        piv_pos = find_pivot_from_row(table)
        table = compute_new_tableau(piv_pos, table)
        return table, piv_pos
    """

    @staticmethod
    def simplex_step(table):
        piv_pos = find_pivot(table)
        table = compute_new_tableau(piv_pos, table)
        return table, piv_pos

    @staticmethod
    def _to_canonical(table, base_indices):

        for i in base_indices:
            obj_fct_val = table[-1, i]
            if obj_fct_val != 0:
                a = table[base_indices.index(i), :]
                b = table[-1, :]
                table[-1, :] = b - obj_fct_val * a
            assert table[-1, i] == 0

        return table

    @staticmethod
    def run_simplex_iteratively(table, var_names, base_indices):

        initial_solution = table_solution_from_base_indices(table, var_names, base_indices)

        yield initial_solution

        table = Optimization._to_canonical(table, base_indices)

        while is_not_final_tableau(table):
            table, piv_pos = Optimization.simplex_step(table)
            base_indices[piv_pos[0]] = piv_pos[1]
            sol = table_solution_from_base_indices(table, var_names, base_indices)
            yield sol

        return table

    @staticmethod
    def full_simplex(table, var_names, base_indices):
        # assert base_variables_are_zero_in_objective_function(table)
        table = Optimization._to_canonical(table, base_indices)

        while is_not_final_tableau(table):
            table, piv_pos = Optimization.simplex_step(table)
            base_indices[piv_pos[0]] = piv_pos[1]

        return table, base_indices

    def run(self, tableau: PlainTableau):
        # INTIALIZE BASE SOLUTION (INDICES / COLUMN IN TABLE).
        initial_solution = tableau.base_var_indices
        try:
            final_table, final_base = self.full_simplex(tableau.table, tableau.var_names, initial_solution)
        except UnboundedTableau:
            return "unbounded", tableau.table

        val = PlainTableau(
            final_table, var_names=tableau.var_names,
            model_vars=tableau._model_vars, base_var_indices=final_base
        ).collect_result()

        return val, final_table

    @classmethod
    def max(cls, table: PlainTableau, output='summary'):
        val, table = Optimization().run(table)

        if output == 'table':
            return table
        else:
            if val == "unbounded":
                return val, {}

            res = _round_result(val._as_dict())

            max_ = table[-1, -1]
            return max_, res

    @classmethod
    def min(cls, tableau: PlainTableau, output='summary'):
        val, table = Optimization().run(tableau.convert_min())

        if output == 'table':
            return table
        else:
            min_ = table[-1, -1] * -1
            return min_, _round_result(val._as_dict())
