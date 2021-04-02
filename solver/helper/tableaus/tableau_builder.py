from solver.helper.tableau import _can_add_constraint, _table_rows_columns, _can_add_objective
from solver.helper.tableaus.plain_tableau import PlainTableau
import numpy as np


class TableauBuilder:

    def __init__(self, var=None, cons=None):
        self.constraints = []
        self.objective = None

        self.no_vars = var
        self.no_cons = cons
        self._table = None

        self._var_names = None

        # self.row_counter = 0
        self._result_table = None

    def with_var_names(self, var_name_array):
        self._var_names = var_name_array
        return self

    @property
    def table(self):
        return self._table

    def add_constraint(self, constraint, add_slack_variable=True):

        assert self.no_vars is None or (len(constraint) == self.no_vars + 1)
        if self.no_vars is None:
            self.no_vars = len(constraint) - 1

        self.constraints.append({'constraint': constraint, 'add_slack_variable': add_slack_variable})
        return self

    def set_objective(self, objective):
        assert len(objective) == self.no_vars + 1
        self.objective = objective
        return self

    @staticmethod
    def _build_constraint(table, eq, row_count, add_slack_variable):

        if _can_add_constraint(table):
            lr, lc = _table_rows_columns(table)
            var = lc - lr # number of

            row = table[row_count, :]

            # print(var)
            # print(eq)
            for i in range(len(eq) - 1):
                row[i] = eq[i]
            row[-1] = eq[-1]

            if add_slack_variable:
                row[var + row_count] = 1
            else:
                raise NotImplementedError
            # FIXME this adds a slack variable for each row.
        else:
            print('Cannot add another constraint.')

        return table

    @staticmethod
    def _build_objective(table, eq):
        # table = self.table
        if _can_add_objective(table):
            # eq = simple_convert(eq)
            lr = len(table[:, 0])
            row = table[lr - 1, :]
            i = 0
            while i < len(eq) - 1:
                row[i] = eq[i] * -1
                i += 1
            # row[-2] = 1 # FIXME. This does not seem necessary and might even be wrong. Find explanation.
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')
        return table

    def get(self):
        n_const = len(self.constraints)

        number_of_slack_variables = len([c for c in self.constraints if c['add_slack_variable']])
        names_of_slack_vars = ["_s_%i" % (i+1) for i in range(number_of_slack_variables)]

        self._table = np.zeros((n_const + 1, self.no_vars + number_of_slack_variables + 1))
        # FIXME assumption here: each constraint function adds a slack variable (columns: + self.cons.)
        # the table will contain one row for each constraint + 1 for the objective function
        # one column will be added for the right side
        # one column will be added for the objective # FIXME ???

        row_count = 0
        for constraint_description in self.constraints:
            c = constraint_description['constraint']
            add_slack_variable = constraint_description['add_slack_variable']
            self._table = TableauBuilder._build_constraint(self._table, c, row_count, add_slack_variable)
            row_count += 1

        self._table = TableauBuilder._build_objective(self._table, self.objective)

        if self._var_names is None:
            vnames = ["x_%i" % (i+1) for i in range(self.no_vars)] + names_of_slack_vars
        else:
            vnames = self._var_names + names_of_slack_vars
        return PlainTableau(self._table, var_names=vnames)
