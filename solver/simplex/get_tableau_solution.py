import numpy as np

from solver.helper.tableau import _table_rows_columns
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.solution import VariableValues


def init_tableau_solution(tableau: PlainTableau, var_names=None):

    if var_names is None:
        var_names = init_var_names(tableau)

    table = tableau.table

    n_model_variables = tableau.model_vars

    val = {}

    for i in range(n_model_variables):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == 1.0 and float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[var_names[i]] = table[loc, -1]
        else:
            val[var_names[i]] = 0

    return VariableValues(var_names[:n_model_variables], [val[vn] for vn in var_names[:n_model_variables]])


def tableau_solution(tableau: PlainTableau, var_names=None):
    if var_names is None:
        var_names = init_var_names(tableau)

    table = tableau.table

    # n_model_variables = tableau.model_vars

    val = {}
    #for i in range(tableau.variable_count):
    #    print(i)

    selected_variables = []
    for row in tableau.table[:-1]:
        b = row[-1]
        constraint = row[:-1]
        # print(constraint, b)
        if b < 0:
            varidx_candidates = np.argwhere(row == -1)  # [0][0]
        else:
            varidx_candidates = np.argwhere(row == 1)  # [0][0]

        var_idx = None
        for cdt in varidx_candidates:
            c = cdt[0]
            # print("row", np.abs(table[:-1, c]))
            if np.sum(np.abs(table[:-1, c])) != 1:
                continue
            var_idx = c
        # print("col", var_idx)
        assert var_idx is not None
        selected_variables.append((var_names[var_idx], abs(b)))

    return VariableValues([n for n, _ in selected_variables], [v for _, v in selected_variables])


def init_var_names(tableau: PlainTableau):
    # lr, lc = _table_rows_columns(tableau.table)
    #  n_model_variables = lc - lr
    n_model_variables = tableau.model_vars
    # print(n_model_variables)
    v = []
    for i in range(n_model_variables):
        v.append('x' + str(i + 1))

    return v
