'''
Created on Jun 29, 2014

@author: alexander


Unit tests for the conversion module..
'''

import unittest

from arabic_to_roman_numerals.convert import convert


class ConvertTest(unittest.TestCase):

    # Tests for a value in [1..9] -
    # these are all special cases, so we have a test for each
    
    def test_value_1(self):
        text = "1"
        expected = "I"
        self.assertEqual(convert(text), expected)

    def test_value_2(self):
        text = "2"
        expected = "II"
        self.assertEqual(convert(text), expected)

    def test_value_3(self):
        text = "3"
        expected = "III"
        self.assertEqual(convert(text), expected)

    def test_value_4(self):
        text = "4"
        expected = "IV"
        self.assertEqual(convert(text), expected)

    def test_value_5(self):
        text = "5"
        expected = "V"
        self.assertEqual(convert(text), expected)

    def test_value_6(self):
        text = "6"
        expected = "VI"
        self.assertEqual(convert(text), expected)

    def test_value_7(self):
        text = "7"
        expected = "VII"
        self.assertEqual(convert(text), expected)

    def test_value_8(self):
        text = "8"
        expected = "VIII"
        self.assertEqual(convert(text), expected)

    def test_value_9(self):
        text = "9"
        expected = "IX"
        self.assertEqual(convert(text), expected)



    # Tests for a value in [10..99]
    # the tenths are all special cases,
    # so we have a test for each

    def test_value_10(self):
        text = "10"
        expected = "X"
        self.assertEqual(convert(text), expected)

    def test_value_21(self):
        text = "21"
        expected = "XXI"
        self.assertEqual(convert(text), expected)

    def test_value_32(self):
        text = "32"
        expected = "XXXII"
        self.assertEqual(convert(text), expected)

    def test_value_43(self):
        text = "43"
        expected = "XLIII"
        self.assertEqual(convert(text), expected)

    def test_value_54(self):
        text = "54"
        expected = "LIV"
        self.assertEqual(convert(text), expected)

    def test_value_65(self):
        text = "65"
        expected = "LXV"
        self.assertEqual(convert(text), expected)

    def test_value_76(self):
        text = "76"
        expected = "LXXVI"
        self.assertEqual(convert(text), expected)

    def test_value_87(self):
        text = "87"
        expected = "LXXXVII"
        self.assertEqual(convert(text), expected)

    def test_value_99(self):
        text = "99"
        expected = "XCIX"
        self.assertEqual(convert(text), expected)


#     def test_max(self):
#         text = "3999"
#         expected = "MMMCMXCIX"
#         self.assertEqual(convert(text), expected)
# 
#     # test example from specification
# 
#     def test_special(self):
#         text = "1903"
#         expected = "MCMIII"
#         self.assertEqual(convert(text), expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
