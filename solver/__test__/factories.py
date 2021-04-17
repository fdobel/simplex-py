from solver.helper.tableaus.read_from_files import builder_from_file


def tableau_1():
    return builder_from_file("__test__/program1.lp")


def tableau_2():
    return builder_from_file("__test__/program2.lp")


def tableau_3():
    return builder_from_file("__test__/program3.lp")


def tableau_4():
    return builder_from_file("__test__/program4.lp")


def tableau_5():
    return builder_from_file("__test__/program5.lp")


def tableau_unbound():
    return builder_from_file("__test__/program_unbound.lp")


def tableau_no_solution():
    return builder_from_file("__test__/program_no_solution.lp")
