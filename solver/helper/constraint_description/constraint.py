

class Constraint:
    def __init__(self, coeffs, right_side, var_names=None):
        self._coeffs = coeffs
        self._b = right_side
        self._var_names = var_names

    def sign(self):
        raise NotImplementedError

    def __str__(self):
        var_names = self._var_names
        if var_names is None:
            var_names = ["x_%i" % i for i in range(len(self._coeffs))]

        s = ["%.2f*%s" % (float(c), vn) for vn, c in zip(var_names, self._coeffs)]
        return "%s %s %.2f" % (" + ".join(s), self.sign(), self._b)


class LessEqualThan(Constraint):
    def sign(self):
        return "<="


class GreaterEqualThan(Constraint):
    def sign(self):
        return ">="


class Equal(Constraint):
    def sign(self):
        return "="