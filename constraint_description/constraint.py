

class Constraint:
    def __init__(self, coeffs, right_side, var_names=None):
        self._coeffs = coeffs
        self._b = right_side
        self._var_names = var_names

    def sign(self):
        raise NotImplementedError

    @property
    def var_names(self):
        var_names = self._var_names
        if var_names is None:
            var_names = ["x_%i" % i for i in range(len(self._coeffs))]
        return var_names

    def __str__(self):
        s = ["%.2f*%s" % (float(c), vn) for vn, c in zip(self.var_names, self._coeffs)]
        return "%s %s %.2f" % (" + ".join(s), self.sign(), self._b)

    def __len__(self):
        return len(self._coeffs) + 1

    def __getitem__(self, item):
        return (self._coeffs + [self._b]).__getitem__(item)
