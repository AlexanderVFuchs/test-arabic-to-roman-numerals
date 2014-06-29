'''
Created on Jun 29, 2014

@author: alexander
'''

from arabic_to_roman_numerals.convert import convert

if __name__ == '__main__':
    """
    Simple demo of module function with one input.
    """
    arabic_digit = "1903" 
    roman_numeral = convert(arabic_digit)
    print("Demo conversion: arabic numeral '{0}'"
          " is converted to roman numeral '{1}'"
          .format(arabic_digit, roman_numeral))
    
