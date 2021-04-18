

class VariableConstraint:
    pass


class IsNaturalNumber(VariableConstraint):
    def __init__(self, var_name):
        self._var_name = var_name

    @property
    def var_name(self):
        return self._var_name

    def __str__(self):
        return "%s ∈ ℕ" % self._var_name
