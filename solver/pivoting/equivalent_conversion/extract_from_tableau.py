from solver.helper.constraint_description import LessEqualThan
from solver.helper.constraint_description.objective import Max, Min
from solver.simplex.plain_tableau import PlainTableau


def constraints_from(tableau: PlainTableau=None):
    assert tableau is not None

    constraints = []
    table = tableau.table

    # obj = table[-1, :-1]
    for constraint in table[:-1, :]:
        constraints.append(
            LessEqualThan(constraint[:-1], constraint[-1])
        )

    return constraints


def objective_from(tableau: PlainTableau=None):
    table = tableau.table
    obj = table[-1, :-1]

    return Min(obj)


def variable_names_from(tableau: PlainTableau=None):
    return tableau.var_names


def slack_variables_from(tableau: PlainTableau=None):
    obj = tableau.table[-1, :-1]
    import numpy as np
    ps = np.argwhere(obj == 0)
    return [tableau.var_names[u[0]] for u in ps]
    # raise NotImplementedError


def artificial_variables_from(tableau: PlainTableau=None):
    obj = tableau.table[-1, :-1]

    import numpy as np
    ps = np.argwhere(obj > 500)
    return [tableau.var_names[u[0]] for u in ps]

