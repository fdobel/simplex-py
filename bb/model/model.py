

class Model:
    def __init__(self, objective, constraints):
        self.objective = objective
        self.constraints = constraints
    def __str__(self):
        s = ""
        s += "----"
        s += str(self.objective) + "\n"
        for c in self.constraints:
            s += str(c) + "\n"
        s += "----"
        return s
