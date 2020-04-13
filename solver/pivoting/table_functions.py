
def _m_return(m):
    if m >= 0:
        return False
    else:
        return True


def is_not_final_tableau(table):
    no_rows = len(table[:, 0])
    m = min(table[no_rows-1, :-1])
    return m < 0  # not m >= 0


def is_not_final_tableau_r(table):
    m = min(table[:-1, -1])
    return m < 0  # not m >= 0
