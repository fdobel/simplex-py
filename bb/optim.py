from solver.optim import Optimization as SimplexOpt

class ProblemGraph:

    def __init__(self, initial_problem):
        self._problems = [initial_problem]
        self._edges = []
        self._pointer = initial_problem

    def current_problem(self):
        return self._pointer


class Optimization:

    def __init__(self, model):
        self._model = model

    def branch_and_bound(self):
        graph = ProblemGraph(self._model)

        problem_to_solve = graph.current_problem()

        solved = SimplexOpt().max(problem_to_solve)
        print(solved)
