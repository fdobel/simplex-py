import numpy as np


def _table_rows_columns(table):
    lc = len(table[0, :])
    lr = len(table[:, 0])
    return lr, lc


def _update_table(table):
    lr = len(table[:, 0])
    empty = []
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            total += j ** 2
        if total == 0:
            empty.append(total)
    return empty


def _can_add_constraint(table):

    empty = _update_table(table)

    if len(empty) > 1:
        return True
    else:
        return False


def _add_objective(table):
    empty = _update_table(table)

    if len(empty) == 1:
        return True
    else:
        return False


LAST_ROW_IDX = -1


class PlainTableau:
    def __init__(self, table, var_names=None):
        self.__table = table
        self._var_names = var_names

    @property
    def table(self):
        return self.__table

    @property
    def variable_count(self):
        lr, lc = _table_rows_columns(self.__table)
        return lc - 1

    @property
    def var_names(self):
        return self._var_names

    def convert_min(self):
        table = self.table
        table[LAST_ROW_IDX, :-2] = [-1 * i for i in table[-1, :-2]]
        table[LAST_ROW_IDX, -1] = -1 * table[-1, -1]
        return PlainTableau(table)

    def collect_result(self):
        from ..simplex.get_tableau_solution import init_tableau_solution
        val = init_tableau_solution(self)
        return val


class TableauBuilder:

    def __init__(self, var=None, cons=None):
        self.constraints = []
        self.objective = None

        self.var = var
        self.cons = cons
        self._table = None

        # self.row_counter = 0
        self._result_table = None

    @property
    def table(self):
        return self._table

    def add_constraint(self, constraint, add_slack_variable=True):

        assert self.var is None or (len(constraint) == self.var + 1)
        if self.var is None:
            self.var = len(constraint) - 1

        self.constraints.append({'constraint': constraint, 'add_slack_variable': add_slack_variable})
        return self

    def set_objective(self, objective):
        assert len(objective) == self.var + 1
        self.objective = objective
        return self

    @staticmethod
    def _build_constraint(table, eq, row_count, add_slack_variable):

        if _can_add_constraint(table):
            lr, lc = _table_rows_columns(table)
            var = lc - lr - 1

            row = table[row_count, :]

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
        if _add_objective(table):
            # eq = simple_convert(eq)
            lr = len(table[:, 0])
            row = table[lr - 1, :]
            i = 0
            while i < len(eq) - 1:
                row[i] = eq[i] * -1
                i += 1
            row[-2] = 1
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')
        return table

    def get(self):
        n_const = len(self.constraints)

        number_of_slack_variables = len([c for c in self.constraints if c['add_slack_variable']])

        self._table = np.zeros((n_const + 1, self.var + number_of_slack_variables + 2))
        # FIXME assumption here: each constraint function adds a slack variable (columns: + self.cons.)
        # the table will contain one row for each constraint + 1 for the objective function
        # one column will be added for the right side
        # one column will be added for the objective

        row_count = 0
        for constraint_description in self.constraints:
            c = constraint_description['constraint']
            add_slack_variable = constraint_description['add_slack_variable']
            self._table = TableauBuilder._build_constraint(self._table, c, row_count, add_slack_variable)
            row_count += 1

        self._table = TableauBuilder._build_objective(self._table, self.objective)

        return PlainTableau(self._table)
