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


    # Tests for a value in [100..999]
    # the tenths are all special cases,
    # so we have a test for each

    def test_value_100(self):
        text = "109"
        expected = "CIX"
        self.assertEqual(convert(text), expected)

    def test_value_234(self):
        text = "234"
        expected = "CCXXXIV"
        self.assertEqual(convert(text), expected)

    def test_value_345(self):
        text = "345"
        expected = "CCCXLV"
        self.assertEqual(convert(text), expected)

    def test_value_456(self):
        text = "456"
        expected = "CDLVI"
        self.assertEqual(convert(text), expected)

    def test_value_567(self):
        text = "567"
        expected = "DLXVII"
        self.assertEqual(convert(text), expected)

    def test_value_678(self):
        text = "678"
        expected = "DCLXXVIII"
        self.assertEqual(convert(text), expected)

    def test_value_781(self):
        text = "781"
        expected = "DCCLXXXI"
        self.assertEqual(convert(text), expected)

    def test_value_892(self):
        text = "892"
        expected = "DCCCXCII"
        self.assertEqual(convert(text), expected)

    def test_value_999(self):
        text = "999"
        expected = "CMXCIX"
        self.assertEqual(convert(text), expected)


    # Tests for a value in [1000..3999]

    def test_value_1000(self):
        text = "1000"
        expected = "M"
        self.assertEqual(convert(text), expected)

    def test_value_2222(self):
        text = "2222"
        expected = "MMCCXXII"
        self.assertEqual(convert(text), expected)



    # Tests for some special values
    
    def test_max(self):
        text = "3999"
        expected = "MMMCMXCIX"
        self.assertEqual(convert(text), expected)


    # test example from specification
    def test_value_1903(self):
        text = "1903"
        expected = "MCMIII"
        self.assertEqual(convert(text), expected)


    def test_invalid_0(self):
        text = "0"
        self.assertRaises(Exception, convert, text)

    def test_invalid_01(self):
        text = "01"
        self.assertRaises(Exception, convert, text)

    def test_invalid_0001(self):
        text = "0001"
        self.assertRaises(Exception, convert, text)

    def test_invalid_4000(self):
        text = "4000"
        self.assertRaises(Exception, convert, text)
 

if __name__ == "__main__":
    unittest.main()
