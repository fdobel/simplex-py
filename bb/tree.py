

class Node:

    def compute(self):
        return 42


class BranchAndBound:

    def __init__(self):
        self.problems = []
        self.edges = []

    def run(self, root_problem: Node):
        self.problems.append(root_problem)

        sol = root_problem.compute()

        return sol
