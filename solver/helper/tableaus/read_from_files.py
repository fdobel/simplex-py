from lp_reader.read import read
from solver.helper.constraint_description import GreaterEqualThan, LessEqualThan
from solver.helper.tableaus import TableauBuilder


def builder_from_file(filepath):

    obj, constraints = read(filepath)

    builder = TableauBuilder()
    for left_side, ctype, right_side in constraints:
        if ctype == "<=":
            builder.add_constraint(LessEqualThan(left_side, right_side))
        elif ctype == ">=":
            builder.add_constraint(GreaterEqualThan(left_side, right_side))
        else:
            raise NotImplementedError

    builder.set_objective(obj + [0])
    return builder


def tableau_from_file(filepath):
    return builder_from_file(filepath).get()