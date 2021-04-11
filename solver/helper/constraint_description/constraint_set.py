from typing import List, Dict

from solver.helper.constraint_description import Constraint


class ConstraintSet:

    def __init__(self, constraints: List[Constraint], var_types=None):
        if var_types is None:
            var_types = {}
        self._constraints = constraints
        self._var_types = var_types

    def __len__(self):
        return self._constraints.__len__()

    def unique_vars(self):
        s = set()
        for c in self._constraints:
            s = s.union(c.var_names)
        return s

    def define_var_type(self, var_name, var_type):
        assert isinstance(var_name, str)
        assert var_type in {'model', 'slack', 'artificial'}
        self._var_types[var_name] = var_type
        return self

    def __type_variables(self, typ_):
        return {var for var, typ in self._var_types.items() if typ == typ_}

    def model_variables(self):
        return self.__type_variables("model")

    def slack_variables(self):
        return self.__type_variables("slack")

    def artificial_variables(self):
        return self.__type_variables("artificial")

    def __str__(self):
        return "\n".join("%s" % c for c in self._constraints)
