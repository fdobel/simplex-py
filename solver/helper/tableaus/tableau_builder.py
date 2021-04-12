from solver.helper.constraint_description import GreaterEqualThan, Constraint, LessEqualThan
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

        self._big_m_value = 1000

    def with_big_m(self, m):
        self._big_m_value = m
        return self

    def with_var_names(self, var_name_array):
        self._var_names = var_name_array
        return self

    @property
    def table(self):
        return self._table

    def add_constraint(self, constraint: Constraint):

        assert self.no_vars is None or (len(constraint) == self.no_vars + 1)
        if self.no_vars is None:
            self.no_vars = len(constraint) - 1

        self.constraints.append(constraint)
        return self

    def set_objective(self, objective):
        assert len(objective) == self.no_vars + 1
        self.objective = objective
        return self

    @staticmethod
    def _build_constraint(eq, add_slack_variable_index, add_artif_var_idx, row_len):
        assert add_slack_variable_index is not None
        # assert not add_artificial_variable  # FIXME NOT YET IMPLEMENTED

        # init new row
        row = np.zeros(row_len)

        if isinstance(eq, GreaterEqualThan):
            slack_variable_factor = -1
        elif isinstance(eq, LessEqualThan):
            slack_variable_factor = 1
        else:
            raise AttributeError

        # copy equation left side
        for i in range(len(eq) - 1):
            row[i] = eq[i]

        # set slack variable at index
        row[add_slack_variable_index] = slack_variable_factor

        # set artificial variable if necessary
        if add_artif_var_idx is not None:
            row[add_artif_var_idx] = 1

        row[-1] = eq[-1]  # right side.

        return row

    @staticmethod
    def _build_objective(table, eq, bigm_indices, optim_direction, big_m):
        # table = self.table
        if _can_add_objective(table):
            # eq = simple_convert(eq)
            lr = len(table[:, 0])
            row = table[lr - 1, :]
            i = 0
            while i < len(eq) - 1:
                if optim_direction == "max":
                    row[i] = eq[i] * -1
                else:
                    row[i] = eq[i]
                i += 1

            for idx in bigm_indices:
                M = big_m
                row[idx] = M
            # row[-2] = 1 # FIXME. This does not seem necessary and might even be wrong. Find explanation.
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')
        return table

    def init_needed_variables(self):
        n_const = len(self.constraints)

        model_variable_indices = [idx for idx in range(self.no_vars)]

        # add slack variable for each constraint (all constraints equal to right side)
        number_of_slack_variables = n_const

        # SLACK VARIABLES
        slack_variable_indices = \
            [idx+self.no_vars for idx in range(n_const)]
        constraint_idx_to_slack_var_idx = {
            idx: idx + self.no_vars for idx in range(n_const)
        }

        # ARTIFICIAL VARIABLES
        greater_equal_constraints_indices = [
            idx for idx, c in enumerate(self.constraints) if isinstance(c, GreaterEqualThan)
        ]
        number_of_artificial_variables = len(greater_equal_constraints_indices)
        artificial_variable_indices = \
            [
                artif_var_idx+self.no_vars+number_of_slack_variables
                for artif_var_idx, constraint_idx in enumerate(greater_equal_constraints_indices)
            ]
        constraint_idx_to_artificial_idx = {}
        art_c = 0
        for c_idx, c in enumerate(self.constraints):
            if isinstance(c, GreaterEqualThan):
                constraint_idx_to_artificial_idx[c_idx] = self.no_vars + number_of_slack_variables + art_c
                art_c += 1

        artif_vars = ["_a_%i" % (i+1) for i in range(number_of_artificial_variables)]
        slack_vars = ["_s_%i" % (i+1) for i in range(number_of_slack_variables)]

        self._table = np.zeros((n_const + 1, self.no_vars + number_of_slack_variables + number_of_artificial_variables + 1))
        # the table will contain one row for each constraint + 1 for the objective function
        # one column will be added for the right side

        if self._var_names is None:
            vnames = ["x_%i" % (i+1) for i in range(self.no_vars)] + slack_vars + artif_vars
        else:
            vnames = self._var_names + slack_vars + artif_vars

        variable_indices = [(index, 'model') for index in model_variable_indices] + \
                           [(index, 'slack') for index in slack_variable_indices] + \
                           [(index, 'artificial') for index in artificial_variable_indices]
        variable_descriptions = [(idx, name, typ_) for (idx, typ_), name in zip(variable_indices, vnames)]

        return constraint_idx_to_slack_var_idx, constraint_idx_to_artificial_idx, variable_descriptions



    def get(self, optim="max"):

        constraint_idx_to_slack_var_idx, \
            constraint_idx_to_artificial_idx, \
            variable_descriptions = self.init_needed_variables()
        vnames = [name for idx, name, _ in variable_descriptions]

        base_var_idxs = []
        for constraint_idx, c in enumerate(self.constraints):

            # get slack variable (index) for constraint
            slack_var_idx = constraint_idx_to_slack_var_idx[constraint_idx]

            if isinstance(c, GreaterEqualThan):  # add artificial variable.
                artif_var_idx = constraint_idx_to_artificial_idx[constraint_idx]
                # add artifvar to initial base
                base_var_idxs.append(artif_var_idx)
            elif isinstance(c, LessEqualThan):
                base_var_idxs.append(slack_var_idx)
                artif_var_idx = None
            else:
                raise AttributeError

            new_row = TableauBuilder._build_constraint(
                c, slack_var_idx, artif_var_idx, len(self._table[-1, :])
            )
            self._table[constraint_idx, :] = new_row

        bigm_indices = [indx for indx, name, typ_ in variable_descriptions if typ_ == "artificial"]
        self._table = TableauBuilder._build_objective(self._table, self.objective, bigm_indices, optim, self._big_m_value)

        return PlainTableau(
            self._table, var_names=vnames,
            model_vars=[vnames[i] for i in range(self.no_vars)],
            base_var_indices=base_var_idxs
        )
