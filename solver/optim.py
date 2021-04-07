
from solver.pivoting.pivot import find_pivot_from_row, find_pivot
from solver.pivoting.table_functions import is_not_final_tableau_r, is_not_final_tableau

import numpy as np

from solver.pivoting.unbounded_tableau_exception import UnboundedTableau
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.get_tableau_solution import tableau_solution, table_solution_from_base_indices


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

    @staticmethod
    def do_simplex_step(table):
        piv_pos = find_pivot_from_row(table)
        table = compute_new_tableau(piv_pos, table)
        return table, piv_pos

    @staticmethod
    def do_simplex_step2(table):
        piv_pos = find_pivot(table)
        table = compute_new_tableau(piv_pos, table)
        return table, piv_pos

    @staticmethod
    def run_simplex_iteratively(table, var_names, initial_base_indices):
        base_indices = initial_base_indices
        # initial_solution = tableau_solution(table, var_names=var_names)
        initial_solution = table_solution_from_base_indices(table, var_names, base_indices)

        yield initial_solution
        # print(table)
        # print(base_indices)
        while is_not_final_tableau_r(table):
            table, piv_pos = Optimization.do_simplex_step(table)
            base_indices[piv_pos[0]] = piv_pos[1]
            sol = table_solution_from_base_indices(table, var_names, base_indices)
            # tableau_solution(table, var_names=var_names)
            # print(sol)
            yield sol
        # print("--")
        print(base_indices)
        while is_not_final_tableau(table):
            table, piv_pos = Optimization.do_simplex_step2(table)
            print("AAA")
            print(table)
            print(piv_pos)
            base_indices[piv_pos[0]] = piv_pos[1]
            print(base_indices)
            sol = table_solution_from_base_indices(table, var_names, base_indices)
            print(sol)
            yield sol  # tableau_solution(table, var_names=var_names)

        return table

    @staticmethod
    def run_simplex(table, var_names):
        while is_not_final_tableau_r(table):
            table, piv_pos = Optimization.do_simplex_step(table)

        while is_not_final_tableau(table):
            table, piv_pos = Optimization.do_simplex_step2(table)

        return table

    def run(self, tableau: PlainTableau):
        # INTIALIZE BASE SOLUTION (INDICES / COLUMN IN TABLE).
        initial_solution = tableau.base_var_indices
        print("Initial", initial_solution)

        try:
            final_table = self.run_simplex(tableau.table, var_names=tableau.var_names)
        except UnboundedTableau:
            return "unbounded", tableau.table

        val = PlainTableau(final_table, model_vars=tableau._model_vars, base_var_indices=tableau.base_var_indices).collect_result()

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
