

class VariableValues:

    def __init__(self, var_names, var_values):
        self._var_names = var_names
        self._var_values = var_values

    def __str__(self):
        return ";".join(["%s:%s" % (n, str(v)) for n, v in zip(self._var_names, self._var_values)])
