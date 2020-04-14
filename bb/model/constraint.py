
class AbstractPlainConstraint:

    def __init__(self, coefficients, right_side):
        self._coefficients = coefficients
        self._right_side = right_side

    @property
    def coefficients(self):
        return self._coefficients

    @property
    def right_side(self):
        return self._right_side

    def __str__(self):
        return str(self._coefficients) + str(self.t) + str(self._right_side)



class SmallerThanConstraint(AbstractPlainConstraint):
    t = "<="

    def as_smaller_than_constraint(self):
        return [self]


class GreaterThanConstraint(AbstractPlainConstraint):
    t = ">="

    def as_smaller_than_constraint(self):
        coeffs = [-coeff for coeff in self._coefficients]
        rs = - self._right_side
        return [
            SmallerThanConstraint(coeffs, rs)
        ]


class EqualsConstraint(AbstractPlainConstraint):
    t = "=="

    def as_smaller_than_constraint(self):
        raise NotImplementedError("nyi")


class IntegerConstraint:
    def __init__(self, variable):
        self.__variable = variable

    @property
    def variable(self):
        return self.__variable

    def __str__(self):
        return "I: " + self.__variable

    def as_smaller_than_constraint(self):
        return []
