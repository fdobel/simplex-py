import numpy as np

from solver.helper.tableau import _table_rows_columns
from solver.helper.tableaus import PlainTableau


def init_tableau_solution(tableau: PlainTableau, var_names=None):

    if var_names is None:
        var_names = init_var_names(tableau)

    table = tableau.table
    lrows, lcols = _table_rows_columns(table)
    n_model_variables = lcols - lrows

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

    return val


def init_var_names(tableau: PlainTableau):
    lr, lc = _table_rows_columns(tableau.table)
    n_model_variables = lc - lr
    v = []
    for i in range(n_model_variables):
        v.append('x' + str(i + 1))
    return v
