from typing import List

from solver.simplex.solution import VariableValues

LAST_ROW_IDX = -1


class SparseTableau:
    def __init__(self, table, var_names=None, model_vars=None, base_var_indices=None):
        assert isinstance(model_vars, list)  # is not None
        assert base_var_indices is not None
        assert var_names is not None
        self._model_vars: List[str] = model_vars
        self.__table = table
        self._var_names: List[str] = var_names
        self._base_var_indices: List[int] = base_var_indices

    @property
    def base_var_indices(self):
        return self._base_var_indices

    @property
    def objective_function(self):
        return self.__table[-1, :-1]

    @property
    def model_vars(self) -> list:
        return self._model_vars

    @property
    def table(self):
        return self.__table

    @property
    def var_names(self) -> list:
        return self._var_names

    def is_canonical(self):
        """
        checks whether all base index variables equal zero in objective function
        :return:
        """
        is_canonical = True
        for i in self._base_var_indices:

            obj_fct_val = self.table[-1, i]
            if obj_fct_val != 0:
                is_canonical = False

        return is_canonical

    def var_result(self, only_model_vars=False) -> VariableValues:
        from solver.simplex.get_tableau_solution import table_solution_from_base_indices
        val = table_solution_from_base_indices(self.table, self._var_names, self.base_var_indices)

        if only_model_vars:
            return VariableValues(self._model_vars, [(val[m] if m in val else 0) for m in self._model_vars])
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