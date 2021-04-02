
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


def _can_add_objective(table):
    empty = _update_table(table)

    if len(empty) == 1:
        return True
    else:
        return False

