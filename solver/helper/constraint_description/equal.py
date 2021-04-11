from .constraint import Constraint


class Equal(Constraint):
    def sign(self):
        return "="
