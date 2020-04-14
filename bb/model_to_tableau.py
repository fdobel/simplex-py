from bb.model.constraint import SmallerThanConstraint
from solver.helper.tableau import TableauBuilder


def smaller_than_to_array(smaller_than: SmallerThanConstraint):
    a = [c for c in smaller_than.coefficients]
    a.append(smaller_than.right_side)
    return a


def model_to_tableau(model):
    builder = TableauBuilder()

    for model_constraint in model.constraints:
        cs = model_constraint.as_smaller_than_constraint()

        for c in cs:
            # print(smaller_than_to_array(c))
            builder.add_constraint(smaller_than_to_array(c))

    obj = [c for c in model.objective]
    builder.set_objective(obj + [0])
    return builder.get()