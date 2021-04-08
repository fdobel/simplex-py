import numpy as np

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


def table_solution_from_base_indices(table, var_names, base_indices):
    _var_names = []
    var_values = []
    # print()
    for bind in base_indices:
        col = table[:-1, bind]
        row_ind = np.argwhere((-1e-9 >= col) | (col >= 1e-9))[0][0]

        b = table[row_ind, -1]
        var_value = b / col[row_ind]
        # print(col, var_value)
        _var_names.append(var_names[bind])
        var_values.append(var_value)

    return VariableValues(_var_names, var_values)

"""
def tableau_solution(table, var_names=None):
    fr = table[0]
    assert len(fr) == len(var_names) + 1

    selected_variables = []
    for row in table[:-1]:
        b = row[-1]
        constraint = row[:-1]
        if b < 0:
            varidx_candidates = np.argwhere((-1-1e-9 <= constraint) & (constraint <= -1 + 1e-9))  # [0][0]
        else:
            varidx_candidates = np.argwhere((1-1e-9 <= constraint) & (constraint <= 1 + 1e-9))  # [0][0]
        # print(constraint, b)
        var_idx = None
        # print("FIND CANDIDATES", varidx_candidates)
        for cdt in varidx_candidates:
            c = cdt[0]
            col_sum = np.sum(np.abs(table[:-1, c]))
            # print(col_sum)
            if col_sum < 1-1e-9 or 1+1e-9 < col_sum:
                continue
            var_idx = c

        assert var_idx is not None
        selected_variables.append((var_names[var_idx], abs(b)))

    return VariableValues([n for n, _ in selected_variables], [v for _, v in selected_variables])
"""


def init_var_names(tableau: PlainTableau):
    n_model_variables = tableau.model_vars
    v = []
    for i in range(n_model_variables):
        v.append('x' + str(i + 1))
    return v
