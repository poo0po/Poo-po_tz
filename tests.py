import unittest

import math

from tz import my_file


class Test(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(min(self.my_file), tz.mini(self.my_file))


    def test_maximum(self):
        self.assertEqual(max(self.my_file), tz.maxi(self.my_file))


    def test_slogenie(self):
        self.assertEqual(sum(self.my_file), tz.result(self.my_file))


    def test_umnogenie(self):
        self.assertEqual(math.prod(self.my_file), tz.product(self.my_file))
