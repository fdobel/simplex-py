from typing import List

from solver.helper.constraint_description import Constraint


class ConstraintSet:

    def __init__(self, constraints: List[Constraint]):
        self._constraints = constraints

    def __len__(self):
        return self._constraints.__len__()

    def unique_vars(self):
        s = set()
        for c in self._constraints:
            s = s.union(c.var_names)
        return s

    def __str__(self):
        return "\n".join("%s" % c for c in self._constraints)
