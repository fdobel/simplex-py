from constraint_description import LessEqualThan
from constraint_description import Objective
from solver.simplex.plain_tableau import PlainTableau

import numpy as np


def _find_slack_variables(tableau: PlainTableau):
    sv = set()
    obj = tableau.objective_function

    for c, val in enumerate(obj):
        col = tableau.table[:-1, c]
        if val == 0.0 and np.sum(col != 0.0) == 1 and np.sum(col == 0.0) == len(col)-1:
            sv.add(tableau.var_names[c])

    return sv


def _find_artificial_variables(tableau: PlainTableau):
    av = set()
    obj = tableau.objective_function

    for c, val in enumerate(obj):
        col = tableau.table[:-1, c]
        if val >= 500.0 and np.sum(col != 0.0) == 1 and np.sum(col == 0.0) == len(col)-1:
            av.add(tableau.var_names[c])

    return av



def to_lp_description(tableau: PlainTableau):
    constr_descr = []

    for row in tableau.table[:-1]:
        cstr = LessEqualThan(row[:-1], row[-1], var_names=tableau.var_names)
        constr_descr.append(cstr)

    objective_row = tableau.table[-1]
    objective = Objective(objective_row[:-1], var_names=tableau.var_names)

    slack_variables = _find_slack_variables(tableau)
    artificial_vars = _find_artificial_variables(tableau)

    return objective, constr_descr, slack_variables, artificial_vars

