from solver.helper.constraint_description.constraint import LessEqualThan
from solver.helper.constraint_description.objective import Min
from solver.helper.tableaus import PlainTableau


def stringify(tableau: PlainTableau):
    descriptors = []

    for row in tableau.table[:-1]:
        cstr = LessEqualThan(row[:-1], row[-1])
        descriptors.append(cstr)

    objective_row = tableau.table[-1]
    descriptors.append(Min(objective_row[:-1]))

    return descriptors

