import numpy as np

from solver.helper.tableau import _table_rows_columns
from solver.simplex.plain_tableau import PlainTableau
from solver.simplex.solution import VariableValues


def init_tableau_solution(tableau: PlainTableau, var_names=None):

    if var_names is None:
        var_names = init_var_names(tableau)

    table = tableau.table
    # lrows, lcols = _table_rows_columns(table)

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

    return VariableValues()


def init_var_names(tableau: PlainTableau):
    # lr, lc = _table_rows_columns(tableau.table)
    #  n_model_variables = lc - lr
    n_model_variables = tableau.model_vars
    # print(n_model_variables)
    v = []
    for i in range(n_model_variables):
        v.append('x' + str(i + 1))

    return v
