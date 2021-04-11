

import unittest

from solver.helper.constraint_description import GreaterEqualThan, LessEqualThan
from .. import TableauBuilder


class Test(unittest.TestCase):

    def test_str(self):
        builder = TableauBuilder()

        self.tableau = builder\
            .add_constraint(GreaterEqualThan([2, 5], 30))\
            .set_objective([5,10,0])\
            .with_var_names(["t1", "t2"])\
            .get()
        self.assertEqual(str(self.tableau), "[t1, t2, _s_1]\n[-2.0, -5.0, -1.0, -30.0]\n[-5.0, -10.0, 0.0, 0.0]")