from solver.helper.tableau import _can_add_constraint, _table_rows_columns, _can_add_objective
from solver.simplex.plain_tableau import PlainTableau
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

        right_side = constraint[len(constraint) - 1]


        self.constraints.append({'constraint': constraint,
                                 'add_slack_variable': add_slack_variable,
                                 'add_artificial_variable': right_side < 0
                                 })
        return self

    def set_objective(self, objective):
        assert len(objective) == self.no_vars + 1
        self.objective = objective
        return self

    @staticmethod
    def _build_constraint(table, eq, table_row, add_slack_variable_index, add_artif_var_idx):

        # assert not add_artificial_variable  # FIXME NOT YET IMPLEMENTED

        if _can_add_constraint(table):
            lr, lc = _table_rows_columns(table)
            var = lc - lr  # number of

            row = table[table_row, :]

            # print(var)
            # print(eq)
            for i in range(len(eq) - 1):
                row[i] = eq[i]
            row[-1] = eq[-1]

            if add_slack_variable_index is not None:
                # slack_var_idx = var + table_row
                row[add_slack_variable_index] = 1
            else:
                raise NotImplementedError

            if add_artif_var_idx is not None:
                row[add_artif_var_idx] = -1
            # row = table[table_row, :]
            # FIXME this adds a slack variable for each row.
        else:
            raise AttributeError('Cannot add another constraint.')

        return table

    @staticmethod
    def _build_objective(table, eq, bigm_indices):
        # table = self.table
        if _can_add_objective(table):
            # eq = simple_convert(eq)
            lr = len(table[:, 0])
            row = table[lr - 1, :]
            i = 0
            while i < len(eq) - 1:
                row[i] = eq[i] * -1
                i += 1

            for idx in bigm_indices:
                M = 1000
                row[idx] = M
            # row[-2] = 1 # FIXME. This does not seem necessary and might even be wrong. Find explanation.
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')
        return table

    def get(self, enable_artif_vars=True):
        n_const = len(self.constraints)

        number_of_slack_variables = len([c for c in self.constraints if c['add_slack_variable']])

        number_of_artificial_variables = len([c for c in self.constraints if c['add_artificial_variable'] and enable_artif_vars])

        artif_vars = ["_a_%i" % (i+1) for i in range(number_of_artificial_variables)]

        # assert number_of_artificial_variables == 0
        # FIXME assumption here: each constraint function adds a slack variable (columns: + self.cons.)
        slack_vars = ["_s_%i" % (i+1) for i in range(number_of_slack_variables)]

        self._table = np.zeros((n_const + 1, self.no_vars + number_of_slack_variables + number_of_artificial_variables + 1))
        # the table will contain one row for each constraint + 1 for the objective function
        # one column will be added for the right side

        row_count = 0
        artif_var_count = 0
        slack_var_count = 0
        base_var_idxs = []
        for constraint_description in self.constraints:

            c = constraint_description['constraint']

            added_artif = False
            if constraint_description['add_artificial_variable'] and enable_artif_vars:
                artif_var_idx = self.no_vars + number_of_slack_variables + artif_var_count
                # add artifvar to initial base
                base_var_idxs.append(artif_var_idx)

                artif_var_count += 1
                added_artif = True
            else:
                artif_var_idx = None


            if constraint_description['add_slack_variable']:
                slack_var_idx = self.no_vars + slack_var_count
                if not added_artif:
                    base_var_idxs.append(slack_var_idx)

                slack_var_count += 1
            else:
                slack_var_idx = None

            self._table = TableauBuilder._build_constraint(
                self._table, c, row_count, slack_var_idx, artif_var_idx
            )
            row_count += 1

        bigm_indices = [i for i in
                        range(self.no_vars + number_of_slack_variables,
                              self.no_vars + number_of_slack_variables + number_of_artificial_variables)
                        ]
        self._table = TableauBuilder._build_objective(self._table, self.objective, bigm_indices)

        if self._var_names is None:
            vnames = ["x_%i" % (i+1) for i in range(self.no_vars)] + slack_vars + artif_vars
        else:
            vnames = self._var_names + slack_vars + artif_vars

        base_vars = [vnames[idx] for idx in base_var_idxs]
        return PlainTableau(self._table, var_names=vnames, model_vars=[vnames[i] for i in range(self.no_vars)], base_vars=base_vars)
