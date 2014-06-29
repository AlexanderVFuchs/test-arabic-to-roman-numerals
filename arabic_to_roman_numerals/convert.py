'''
Created on Jun 29, 2014

@author: alexander

Conversion library from arabic to roman numerals.
'''

import re


def convert(arabic_numeral):
    """
Roman numerals

Write a function which returns a Roman numeral string representation of a given
Arabic number.

E.g. if you pass the number 4 to the function, it should return a string
containing "IV". Roman numerals are not strictly unique, but you can adhere
to the following "standard" that can be found on wikipedia:

* A number written in Arabic numerals can be broken into digits.
  For example, 1903 is composed of 1, 9, 0, and 3.
  To write the Roman numeral, each of the non-zero digits should be treated
  separately. In the above example, 1,000 = M, 900 = CM, and 3 = III.
  Therefore, 1903 = MCMIII.

* The symbols I, X, C, and M can be repeated three times in succession,
  but no more. (They may appear more than three times if they appear
  non-sequentially, such as XXXIX.) D, L, and V can never be repeated.

* I can be subtracted from V and X only. X can be subtracted from L and C only.
  C can be subtracted from D and M only. V, L, and D can never be subtracted

* Only one small-value symbol may be subtracted from any large-value symbol.

Signature:
    :param arabic_digit: The arabic numeral input string: [1..3999].
        No leading 0 accepted.
    :returns: Roman numeral representation of arabic_digit 
    :raises: Exception in case of invalid input.
    """
    # check pre-condition: range 1-3999
    if not re.match("[1-3]?[0-9]{0,2}[1-9]", arabic_numeral):
        raise Exception("Invalid Input: {0}".format(arabic_numeral))
    # check pre-condition: no leading 0
    if not re.match("[^0].*", arabic_numeral):
        raise Exception("Invalid Input: {0}".format(arabic_numeral))

    if len(arabic_numeral) >= 1:
        arabic_unit = convert_unit(arabic_numeral[-1])
    else:
        arabic_unit = ""

    if len(arabic_numeral) >= 2:
        arabic_tens = convert_tens(arabic_numeral[-2])
    else:
        arabic_tens = ""
    
    if len(arabic_numeral) >= 3:
        arabic_hundreds = convert_hundreds(arabic_numeral[-3])
    else:
        arabic_hundreds = ""
    
    if len(arabic_numeral) >= 4:
        arabic_thousands = convert_thousands(arabic_numeral[-4])
    else:
        arabic_thousands = ""

    return arabic_thousands + arabic_hundreds + arabic_tens + arabic_unit



def convert_unit(arabic_digit):
    """Helper function.
    
    Converts an arabic unit value to the roman representation.
    
    :param arabic_digit: arabic unit value: [0..9]
    :returns: Roman numeral representation of arabic_digit.
        Returns the empty string for '0'.
    :raises: Exception in case of invalid input.
    """
    if arabic_digit == "0":
        return ""
    elif arabic_digit == "1":
        return "I"
    elif arabic_digit == "2":
        return "II"
    elif arabic_digit == "3":
        return "III"
    elif arabic_digit == "4":
        return "IV"
    elif arabic_digit == "5":
        return "V"
    elif arabic_digit == "6":
        return "VI"
    elif arabic_digit == "7":
        return "VII"
    elif arabic_digit == "8":
        return "VIII"
    elif arabic_digit == "9":
        return "IX"
    else:
        raise Exception("Invalid Input: {0}".format(arabic_digit))


def convert_tens(arabic_digit):
    """Helper function.
    
    Converts the tens digit of an arabic value to the roman representation.
    
    :param arabic_digit: [0..9]
    :returns: Roman numeral representation of arabic_digit
    :raises: Exception in case of invalid input.
    """
    if arabic_digit == "0":
        return ""
    elif arabic_digit == "1":
        return "X"
    elif arabic_digit == "2":
        return "XX"
    elif arabic_digit == "3":
        return "XXX"
    elif arabic_digit == "4":
        return "XL"
    elif arabic_digit == "5":
        return "L"
    elif arabic_digit == "6":
        return "LX"
    elif arabic_digit == "7":
        return "LXX"
    elif arabic_digit == "8":
        return "LXXX"
    elif arabic_digit == "9":
        return "XC"
    else:
        raise Exception("Invalid Input: {0}".format(arabic_digit))


def convert_hundreds(arabic_digit):
    """Helper function.
    
    Converts the hundreds digit of an arabic value to the roman representation.
    
    :param arabic_digit: [0..9]
    :returns: Roman numeral representation of arabic_digit
    :raises: Exception in case of invalid input.
    """
    if arabic_digit == "0":
        return ""
    elif arabic_digit == "1":
        return "C"
    elif arabic_digit == "2":
        return "CC"
    elif arabic_digit == "3":
        return "CCC"
    elif arabic_digit == "4":
        return "CD"
    elif arabic_digit == "5":
        return "D"
    elif arabic_digit == "6":
        return "DC"
    elif arabic_digit == "7":
        return "DCC"
    elif arabic_digit == "8":
        return "DCCC"
    elif arabic_digit == "9":
        return "CM"
    else:
        raise Exception("Invalid Input: {0}".format(arabic_digit))



def convert_thousands(arabic_digit):
    """Helper function.
    
    Converts the thousand digit of an arabic value to the roman representation.
    
    :param arabic_digit: [1..3]
    :returns: Roman numeral representation of arabic_digit
    :raises: Exception in case of invalid input.
    """
    if arabic_digit == "1":
        return "M"
    elif arabic_digit == "2":
        return "MM"
    elif arabic_digit == "3":
        return "MMM"
    else:
        raise Exception("Invalid Input: {0}".format(arabic_digit))

