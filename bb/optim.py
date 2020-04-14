from bb.model.constraint import GreaterThanConstraint, SmallerThanConstraint
from bb.model.model import Model
from bb.model_to_tableau import model_to_tableau
from solver.helper.tableau import PlainTableau
from solver.optim import Optimization as SimplexOpt
import math
import concurrent.futures

from .graph import ProblemGraph


def generate_new_instances(model, value, solution):
    possible_new = set(solution.keys()).intersection(set(model.integer_constraints()))
    for var_name in possible_new:
        var_value = solution[var_name]

        variable_is_integer = float.is_integer(var_value)
        if variable_is_integer:
            continue

        var_selector = [0 for i in model.variable_names()]
        # print("restrict", var_name)
        var_selector[model.index_of_variable(var_name)] = 1
        # print("restrict", var_name, var_selector)
        cons_lt = SmallerThanConstraint(var_selector, math.floor(var_value))
        new_model1 = model.add_constraint(cons_lt)
        # print(cons_lt, new_model1)
        # print("new model 1: ", new_model1)

        cons_gt = GreaterThanConstraint(var_selector, math.ceil(var_value))
        new_model2 = model.add_constraint(cons_gt)

        new_models = [new_model1, new_model2]
        return new_models
    return []


class Optimization:

    def __init__(self, model: Model):
        self._model = model

    def branch_and_bound(self):
        graph = ProblemGraph(self._model)
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

            while not graph.is_finished():

                id, problem_node = graph.current_problem()

                if id >= 20:
                    exit(0)
                print("NEXT PROBLEM:", id)
                tableau_problem = model_to_tableau(problem_node.problem)
                # print(problem_node.problem)
                # print(tableau_problem.table)

                def maxSimplex(prob):
                    return SimplexOpt().max(prob)

                future = executor.submit(maxSimplex, tableau_problem)
                value = -1
                solution = None
                sol_found = False
                try:
                    value, solution = future.result(0.1)
                    sol_found = True
                except concurrent.futures.TimeoutError:
                    print("timeout")
                except RuntimeError:
                    print("no solution")

                print(solution, "=>", value)
                if not sol_found:
                    graph.set_problem_value(id, "infeasible")
                    continue
                #value, solution = SimplexOpt().max(tableau_problem)
                problem_instances = generate_new_instances(problem_node.problem, value, solution)
                graph.queue_problems(problem_instances)

                graph.set_problem_value(id, value)


