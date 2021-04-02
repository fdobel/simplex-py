import numpy as np


class TableauWithObjective:

    def __init__(self, objective, coeffs, right_side):
        self._obj = objective
        self._coeffs = coeffs
        self._right_side = right_side

    @property
    def full_table(self):
        s = np.vstack([self._obj, self._coeffs])
        right_side = np.hstack([np.array([0]), self._right_side])
        right_side = np.atleast_2d(right_side).T
        return np.hstack([s, right_side])

    @property
    def objective(self):
        return self._obj

    @property
    def right_side(self):
        return self._right_side

    def __str__(self):
        return self.full_table.__str__()
