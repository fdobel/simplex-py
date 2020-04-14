
class ProblemNode:
    def __init__(self, id, problem):
        self._id = id
        self._problem = problem
        self._value = None

    @property
    def problem(self):
        return self._problem

    def set_value(self, value):
        self._value = value


class ProblemGraph:

    def __init__(self, initial_problem):
        self._next_id = 0
        id_ = self._next_id
        self._problems = { id_: ProblemNode(id_, initial_problem) }
        self._next_id += 1
        self._edges = []
        self.queue = [id_]

    def __queue_one(self, problem):
        ni = self._next_id
        self._problems[ni] = ProblemNode(ni, problem)
        self.queue.append(ni)
        self._next_id += 1

    def queue_problems(self, problems):
        for p in problems:
            self.__queue_one(p)

    def is_finished(self):
        return len(self.queue) <= 0

    def current_problem(self):
        next_id = self.queue[0]
        return next_id, self._problems[next_id]

    def set_problem_value(self, id_, value):
        self._problems[id_].set_value(value)
        self.queue.remove(id_)
