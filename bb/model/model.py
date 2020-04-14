from bb.model.constraint import IntegerConstraint
import re

class Model:
    def __init__(self, objective, constraints):
        self.objective = objective
        self.constraints = constraints

    def integer_constraints(self):
        return list(map(lambda x: x.variable, filter(lambda x: isinstance(x, IntegerConstraint), self.constraints)))

    def no_variables(self):
        return len(self.objective)

    def variable_names(self):
        return ["x"+str(v) for v in range(self.no_variables())]

    def index_of_variable(self, variable_name):
        return int(re.match(r'x(\d+)', variable_name)[1]) - 1

    def __str__(self):
        s = ""
        s += "----"
        s += str(self.objective) + "\n"
        for c in self.constraints:
            s += str(c) + "\n"
        s += "----"
        return s

    def add_constraint(self, constraint):
        constraints = list([c for c in self.constraints]) + [constraint]
        return Model(self.objective, constraints)