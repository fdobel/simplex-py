from solver.helper.constraint_description import GreaterEqualThan
from solver.helper.constraint_description import LessEqualThan


def obj_string_convert(eq):
    return [float(i) for i in eq.split(',')]


def constr_string_convert(eq):
    eq = eq.split(',')
    if '>=' in eq:
        g = eq.index('>=')
        del eq[g]
        eq = [float(i) for i in eq]
        return GreaterEqualThan(eq[:-1], eq[-1])
    if '<=' in eq:
        l = eq.index('<=')
        del eq[l]
        eq = [float(i) for i in eq]
        return LessEqualThan(eq[:-1], eq[-1])
