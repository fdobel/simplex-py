

class VariableValues:

    def __init__(self, var_names, var_values):
        self._var_names = var_names
        self._var_values = var_values

    @staticmethod
    def from_dict(dct):
        arr = [(n, v) for n, v in dct.items()]

        return VariableValues([n for n, v in arr], [v for n, v in arr])

    def _as_dict(self):
        return {
            vn: vv for  vn, vv in zip(self._var_names, self._var_values)
        }

    def __eq__(self, other):
        if not isinstance(other, VariableValues):
            return False

        return self._as_dict() == other._as_dict()

    def __str__(self):
        return ";".join(["%s:%s" % (n, str(v)) for n, v in zip(self._var_names, self._var_values)])

    @property
    def vars(self):
        return self._var_names
