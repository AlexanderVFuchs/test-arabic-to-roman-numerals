'''
Created on Jun 29, 2014

@author: alexander


Unit tests for the conversion module..
'''

import unittest

from arabic_to_roman_numerals.convert import convert


class ConvertTest(unittest.TestCase):


    def test_min_value(self):
        text = "1"
        expected = "I"
        self.assertEqual(convert(text), expected)

    def test_one(self):
        text = "1"
        expected = "I"
        self.assertEqual(convert(text), expected)

    def test_two(self):
        text = "2"
        expected = "II"
        self.assertEqual(convert(text), expected)

    def test_three(self):
        text = "3"
        expected = "III"
        self.assertEqual(convert(text), expected)

    def test_four(self):
        text = "4"
        expected = "IV"
        self.assertEqual(convert(text), expected)

    def test_five(self):
        text = "5"
        expected = "V"
        self.assertEqual(convert(text), expected)

    def test_six(self):
        text = "6"
        expected = "VI"
        self.assertEqual(convert(text), expected)

    def test_seven(self):
        text = "7"
        expected = "VII"
        self.assertEqual(convert(text), expected)

    def test_eight(self):
        text = "8"
        expected = "VIII"
        self.assertEqual(convert(text), expected)

    def test_nine(self):
        text = "9"
        expected = "IX"
        self.assertEqual(convert(text), expected)


    def test_special(self):
        text = "1903"
        expected = "MCMIII"
        self.assertEqual(convert(text), expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
