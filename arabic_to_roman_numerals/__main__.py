'''
Created on Jun 29, 2014

@author: alexander
'''

from arabic_to_roman_numerals.convert import convert

if __name__ == '__main__':
    arabic_numeral = "1903" 
    roman_numeral = convert(arabic_numeral)
    print("Demo conversion: arabic numeral '{0}'"
          " is converted to roman numeral '{1}'"
          .format(arabic_numeral, roman_numeral))
    
