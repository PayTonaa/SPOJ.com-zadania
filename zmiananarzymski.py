# Create a RomanNumerals class that can convert a roman to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").


import math

def to_roman(val):
    wynik = ""
    val = str(val)
    if len(val) == 4:
        wynik += str(math.floor(chr(val[1])))
    return wynik
def from_roman(roman_num):
    wynik = 0
    roman_num = list(roman_num)
    for x in range(0, len(roman_num)):
        if roman_num[x] == "I":
            wynik += 1
        if roman_num[x] == "V":
            wynik += 5
        if roman_num[x] == "X":
            wynik += 10
        if roman_num[x] == "L":
            wynik += 50
        if roman_num[x] == "C":
            wynik += 100
        if roman_num[x] == "D":
            wynik += 500
        if roman_num[x] == "M":
            wynik += 1000
        
        
    return wynik
    

val = 1111
roman_num = "XXI"
print(to_roman(val), from_roman(roman_num))
