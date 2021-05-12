from constraint_description import ConstraintSet, Objective
from solver.helper.tableaus import TableauBuilder
from solver.simplex.plain_tableau import PlainTableau


def transform(cs: ConstraintSet, obj: Objective):
    tb = TableauBuilder()
    for c in cs.constraints:
        tb.add_constraint(c)

    tb.set_objective(obj._coeffs)

    return tb.get()
