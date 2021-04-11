from .constraint import Constraint


class GreaterEqualThan(Constraint):
    def sign(self):
        return ">="

