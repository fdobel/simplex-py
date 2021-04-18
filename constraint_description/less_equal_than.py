from .constraint import Constraint


class LessEqualThan(Constraint):
    def sign(self):
        return "<="