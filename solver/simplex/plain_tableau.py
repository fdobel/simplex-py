from solver.helper.tableau import _table_rows_columns
from solver.simplex.solution import VariableValues

LAST_ROW_IDX = -1


class PlainTableau:
    def __init__(self, table, var_names=None, model_vars=None, base_var_indices=None):
        assert isinstance(model_vars, list)  # is not None
        assert base_var_indices is not None
        self._model_vars = model_vars
        self.__table = table
        self._var_names = var_names
        self._base_var_indices = base_var_indices

    @property
    def base_var_indices(self):
        return self._base_var_indices  # return [idx for var_name, idx in zip(self._var_names, range(len(self._var_names))) if var_name in self._base_vars]

    @property
    def objective_function(self):
        return self._var_names, self.__table[-1, :-1]

    @property
    def model_vars(self) -> int:
        return len(self._model_vars)

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
        return PlainTableau(table, var_names=self.var_names, model_vars=self._model_vars, base_var_indices=self._base_var_indices)

    def collect_result(self) -> VariableValues:
        from solver.simplex.get_tableau_solution import init_tableau_solution
        val = init_tableau_solution(self, var_names=self.var_names)
        return val

    def intermediate_solution(self) -> VariableValues:
        from solver.simplex.get_tableau_solution import tableau_solution, table_solution_from_base_indices
        val = table_solution_from_base_indices(self.table, self._var_names, self.base_var_indices)
        # val = tableau_solution(self.table, var_names=self.var_names)
        return val

    def __str__(self):
        s = ""
        if self._var_names is not None:
            s += "[%s]" % ", ".join(self.var_names) + "\n"

        row_strings = []
        for row in self.table:
            row_strings.append(str(list(row)))
        s += "\n".join(row_strings)
        return s