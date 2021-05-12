from constraint_description import ConstraintSet, Objective
from solver.optim import Optimization
from solver.tableau_from_constraint_description import transform


def compute(constraint_set: ConstraintSet, optim_func: Objective):
    branch_variables = constraint_set.variable_constraints
    for v in branch_variables:
        print(v)

    # solve  without branch.
    res, sol = Optimization.max(transform(constraint_set, optim_func))
    print(res, sol)

    return 42.0
