import unittest
from solver.helper.convert import constr_string_convert, obj_string_convert
from solver.helper.tableaus import TableauBuilder

from solver.optim import Optimization


class Test(unittest.TestCase):

    def setUp(self):
        self.t3 = TableauBuilder()
        self.t3.add_constraint(constr_string_convert('2,1,<=,18')).\
            add_constraint(constr_string_convert('2,3,<=,42')). \
            add_constraint(constr_string_convert('3,1,<=,24')).\
            set_objective(obj_string_convert('3,2,0'))

    def test_example4(self):
        t = self.t3.get()


