from typing import List

from constraint_description import Constraint
from constraint_description.conventions import PositiveVariables


class ConstraintSet:

    def __init__(self, constraints: List[Constraint], variable_constraints: List=[], var_types=None, conventions=[PositiveVariables]):
        if var_types is None:
            var_types = {}
        self._constraints = constraints
        self._var_constraints = variable_constraints
        self._var_types = var_types
        self._conventions = conventions

    def __len__(self):
        return self._constraints.__len__()

    def __iter__(self):
        for constr in self._constraints:
            yield constr

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

    @property
    def variable_constraints(self):
        return self._var_constraints

    @property
    def constraints(self):
        return self._constraints

    def __str__(self):
        s = "\n".join("%s" % c for c in self._constraints)
        for var_constr in self._var_constraints:
            s  += "\n"  + str(var_constr)
        if PositiveVariables in self._conventions:
            s += "\n" + "all variables positive"
        return s
