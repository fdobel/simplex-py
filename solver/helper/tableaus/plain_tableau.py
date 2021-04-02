from solver.helper.tableau import _table_rows_columns

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
        from ...simplex.get_tableau_solution import init_tableau_solution
        val = init_tableau_solution(self)
        return val