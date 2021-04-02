
def _m_return(m):
    if m >= 0:
        return False
    else:
        return True


def is_not_final_tableau(table):
    m = min(table[-1, :-1])  # minimum last row <=> minimum objective fct. coeffs
    return m < 0  # <=> not m >= 0


def is_not_final_tableau_r(table):
    # print(table, table[:-1, -1])
    # print(table.shape, table[:-1, -1].shape)
    m = min(table[:-1, -1])  # minimum last column. <=> minimum right side.
    return m < 0  # <=> not m >= 0
