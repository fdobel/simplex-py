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


def _add_constraint(table):

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
    def __init__(self, table, column_names=None):
        self.__table = table

        lr, lc = _table_rows_columns(table)
        n_model_variables = lc - lr - 1

        if column_names is None:
            v = []
            for i in range(n_model_variables):
                v.append('x' + str(i + 1))
            for i in range(lc - n_model_variables - 1):
                v.append('s' + str(i + 1))
            self._column_names = v
        else:
            self._column_names = column_names

    @property
    def table(self):
        return self.__table

    @property
    def right_side(self):
        return self.__table[:, -1]

    def convert_min(self):
        table = self.table
        table[LAST_ROW_IDX, :-2] = [-1 * i for i in table[-1, :-2]]
        table[LAST_ROW_IDX, -1] = -1 * table[-1, -1]
        return PlainTableau(table)

    def column_names(self):
        return self._column_names

    """
    def variable_values(self):
        lrows, lcols = _table_rows_columns(self.table)
        for i in range(lcols):
            col = self.table[:, i]
            s = sum(col)
            m = max(col)
            if s == m:
    """

    def basis_indices(self):
        base_ids = set()

        n_var_cols = len(self._column_names)
        for i in range(n_var_cols):
            col = self.table[:, i]
            if float(sum(col)) == 1.0:
                base_ids.add(i)
        return base_ids

    def current_solution(self):
        table = self.__table

        lrows, lcols = _table_rows_columns(table)

        val = {}
        bi = self.basis_indices()

        for i in range(len(self._column_names)):
            if i in bi:
                col = table[:, i]
                row_idx = np.where(col != 0.0)[0][0]
                val[self._column_names[i]] = col[row_idx] * self.right_side[row_idx]
            else:
                val[self._column_names[i]] = 0.0
        print(val)
        return val

    def __str__(self):
        return str(self.column_names()) + " " + str(self.__table)


class TableauBuilder:

    def __init__(self, var=None, cons=None):
        self.constraints = []
        self.objective = None

        self.no_modelvars = var
        self.cons = cons
        self._table = None

        self._result_table = None

    @property
    def table(self):
        return self._table

    def add_greater_than(self, constraint):
        assert self.no_modelvars is None or (len(constraint) == self.no_modelvars + 1)
        if self.no_modelvars is None:
            self.no_modelvars = len(constraint) - 1
        self.constraints.append({ 'type': '>=', 'constraint': constraint })

    def add_smaller_than(self, constraint):
        assert self.no_modelvars is None or (len(constraint) == self.no_modelvars + 1)
        if self.no_modelvars is None:
            self.no_modelvars = len(constraint) - 1

        self.constraints.append({ 'type': '<=', 'constraint': constraint })

    def add_constraint(self, constraint):
        self.add_smaller_than(constraint)

    def set_objective(self, objective):

        assert len(objective) == self.no_modelvars + 1

        self.objective = objective

    def _build_constraint(self, table, tableau_description, const, curr_row, curr_greater_than):
        mvars = tableau_description['mvars']
        svars = tableau_description['svars']

        ctype = const['type']
        eq = const['constraint']

        if _add_constraint(table):
            row = table[curr_row, :]

            for i in range(len(eq) - 1):
                row[i] = eq[i]
            row[-1] = eq[-1]

            if ctype == '<=':
                row[mvars + curr_row] = 1
            elif ctype == '>=':
                # negative slack variable
                row[mvars + curr_row] = -1
                # add artificial var
                row[mvars + svars + curr_greater_than - 1] = 1
            else:
                raise RuntimeError("wrong constraint type")
        else:
            print('Cannot add another constraint.')

    def _build_objective(self, table, eq, art_vars_pointer, bigM):

        if _add_objective(table):
            # eq = simple_convert(eq)
            lr = len(table[:, 0])
            row = table[lr - 1, :]
            i = 0
            while i < len(eq) - 1:
                row[i] = eq[i] * -1
                i += 1

            i = art_vars_pointer
            while i < len(table[0, :]) - 1:
                row[i] = bigM
                i += 1
            row[-2] = 1
            row[-1] = eq[-1]
        else:
            print('You must finish adding constraints before the objective function can be added.')

    def get(self):
        self.cons = len(self.constraints)
        no_slack_vars = self.cons
        no_objective_rows = 1
        no_artif_variables = len([1 for c in self.constraints if c['type'] == '>='])
        tableau_description = { 'mvars': self.no_modelvars, "svars": no_slack_vars, "avars":no_artif_variables }
        t = np.zeros(
            (
                self.cons + no_objective_rows,  # tableau rows
                self.no_modelvars + no_slack_vars + no_artif_variables + no_objective_rows + 1 # tableau cols + 1 right side
            )
        )

        ac = 0
        for row_counter, c in enumerate(self.constraints):
            if c['type'] == '>=':
                ac += 1
            self._build_constraint(t, tableau_description, c, row_counter, ac)

        self._build_objective(t, self.objective, self.no_modelvars + no_slack_vars, 25)

        self._table = t
        print(t)

        return PlainTableau(
            t,
            gen_var_names(self.no_modelvars) +
            gen_var_names(no_slack_vars, prefix="s") +
            gen_var_names(no_artif_variables, prefix="a")
        )


def gen_var_names(n, prefix='x'):
    return  [prefix + str(i + 1) for i in range(n)]