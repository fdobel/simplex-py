from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder


def tableau_1():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('2,-1,>=,10'))\
        .add_constraint(constr_string_convert('1,1,<=,20'))\
        .set_objective(obj_string_convert('5,10,0'))
    return tb


def tableau_2():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('2,5,>=,30'))\
        .add_constraint(constr_string_convert('-3,5,>=,5'))\
        .add_constraint(constr_string_convert('8,3,<=,85'))\
        .add_constraint(constr_string_convert('-9,7,<=,42'))\
        .set_objective(obj_string_convert('2,7,0'))
    return tb


def tableau_3():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('50,24,<=,2400'))\
        .add_constraint(constr_string_convert('30,33,<=,2100'))\
        .add_constraint(constr_string_convert('1,0,>=,45'))\
        .add_constraint(constr_string_convert('0,1,>=,5'))\
        .set_objective(obj_string_convert('1,1,0'))
    # 1, 0 >= 45 <=> -1, 0 <= -45
    return tb


def tableau_4():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('2,1,<=,18'))\
        .add_constraint(constr_string_convert('2,3,<=,42'))\
        .add_constraint(constr_string_convert('3,1,<=,24'))\
        .set_objective(obj_string_convert('3,2,0'))
    return tb


def tableau_6():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('4,4,<=,6'))\
        .add_constraint(constr_string_convert('1,3,>=,2'))\
        .set_objective(obj_string_convert('1,5,0'))
    return tb


def tableau_unbound():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('-1,-1,<=,0'))\
        .set_objective(obj_string_convert('1,1,0'))
    return tb


def tableau_no_solution():
    tb = TableauBuilder()
    tb.add_constraint(constr_string_convert('1,1,>=,1.5')) \
        .add_constraint(constr_string_convert('1,1,<=,1')) \
        .set_objective(obj_string_convert('1,1,0'))
    return tb