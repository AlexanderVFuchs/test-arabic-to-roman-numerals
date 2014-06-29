'''
Created on Jun 29, 2014

@author: alexander
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
    return "1903"

