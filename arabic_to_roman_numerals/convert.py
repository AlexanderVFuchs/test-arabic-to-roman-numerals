'''
Created on Jun 29, 2014

@author: alexander

Conversion library from arabic to roman numerals.
'''


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
    :param arabic_numeral: The arabic numeral input string.
    :returns: Roman numeral representation of arabic_numeral 
    """
    
    # determine Roman representation for unit value
    return convert_unit(arabic_numeral)



def convert_unit(arabic_numeral):
    """Helper function.
    
    Converts an arabic unit value to the roman representation.
    
    :param arabic_numeral: arabic unit value: [1..9]
    :returns: Roman numeral representation of arabic_numeral
    :raises: Exception in case of invalid input.
    """
    if arabic_numeral == "1":
        return "I"
    elif arabic_numeral == "2":
        return "II"
    elif arabic_numeral == "3":
        return "III"
    elif arabic_numeral == "4":
        return "IV"
    elif arabic_numeral == "5":
        return "V"
    elif arabic_numeral == "6":
        return "VI"
    elif arabic_numeral == "7":
        return "VII"
    elif arabic_numeral == "8":
        return "VIII"
    elif arabic_numeral == "9":
        return "IX"
    else:
        raise Exception("Invalid Input: {0}".format(arabic_numeral))

