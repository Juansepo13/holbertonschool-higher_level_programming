#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if not bool(roman_string):
        return 0
    check = isinstance(roman_string, str)
    if check is False:
        return 0
    count = 0
    for i in roman_string:
        a = roman_string[count]
        if count+int(1) < len(roman_string):
            b = roman_string[count+1]
        else:
            b = 'I'
        if int(romans[a]) < int(romans[b]):
            sum -= int(romans[i])
        else:
            sum += int(romans[i])
        count += 1
    return sum
