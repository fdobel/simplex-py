class Objective:
    def __init__(self, coeffs, var_names=None):
        self._coeffs = coeffs
        self._var_names = var_names

    def sign(self):
        return "obj"

    def __str__(self):
        var_names = self._var_names
        if var_names is None:
            var_names = ["x_%i" % i for i in range(len(self._coeffs))]

        s = ["%.2f*%s" % (float(c), vn) for vn, c in zip(var_names, self._coeffs)]
        return "%s %s" % (self.sign(), " + ".join(s))


class Min(Objective):
    def sign(self):
        return "min"


class Max(Objective):
    def sign(self):
        return "max"
