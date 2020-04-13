

def obj_string_convert(eq):
    return [float(i) for i in eq.split(',')]


def constr_string_convert(eq):
    eq = eq.split(',')
    if '>=' in eq:
        g = eq.index('>=')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if '<=' in eq:
        l = eq.index('<=')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

