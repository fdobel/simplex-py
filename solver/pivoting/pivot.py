import numpy as np


def _minimal_positive_pivot(total):
    element = min(
        filter(
            lambda x: x[1] > 0,
            enumerate(total)
        ),
        key=lambda x: x[1]
    )

    if element[1] < 0:
        raise AttributeError("pivot element error")
    return element[1], element[0]


def _pivot_step(piv, right_side):
    if right_side / piv > 0 and piv != 0:
        return right_side / piv
    return 0


def _choose_piv_element_in_column(table, col_idx):
    col = table[:-1, col_idx]
    right_side = table[:-1, -1]  # last column in table

    total = map(lambda pivb: _pivot_step(pivb[0], pivb[1]), zip(col, right_side))

    element, row_idx = _minimal_positive_pivot(total)

    return [row_idx, col_idx]


def find_pivot_from_row(table):
    piv_row = find_pivot_row(table)
    row = table[piv_row, :-1]
    m = min(row)
    col_idx = np.where(row == m)[0][0]
    return _choose_piv_element_in_column(table, col_idx)


def find_pivot(table):
    col_idx = find_pivot_column(table)
    return _choose_piv_element_in_column(table, col_idx)


def find_pivot_row(table):
    last_col_idx = len(table[0, :]) - 1
    m = min(table[:-1, last_col_idx])

    if m <= 0:
        col_idx = np.where(table[:-1, last_col_idx] == m)[0][0]
    else:
        raise AttributeError("No negative element on right side.")
    return col_idx


def find_pivot_column(table):
    last_row_idx = len(table[:, 0]) - 1

    m = min(table[last_row_idx, :-1])

    if m <= 0:
        col_idx = np.where(table[last_row_idx, :-1] == m)[0][0]
    else:
        raise AttributeError("No negative element in objective row.")
    return col_idx
