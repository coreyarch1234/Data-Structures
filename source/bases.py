#!python

import string
from math import *


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    universal_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #create list of characters that can be used
    universal_dict = {}
    count = 0
    for char in universal_list:
        universal_dict[char] = count
        count += 1
    num_by_base = reversed(list(str_num))
    converted_val = 0
    convert_count = 0
    for num in num_by_base:
        converted_val += (base ** convert_count) * (universal_dict[num]) #i.e. (1)2^0 + (0)2^1 + ...
        convert_count += 1
    return converted_val



def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    universal_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #create list of characters that can be used
    universal_dict = {}
    count = 0
    for char in universal_list:
        universal_dict[char] = count
        count += 1
    reverse_universal_dict = dict((v,k) for k,v in universal_dict.iteritems())
    converted_val = ''
    remainder_val = 0

    while num != 0:
        remainder_val = int(num) % int(base) #remainder to be stored
        num = int(num) / int(base) #next number
        converted_val += reverse_universal_dict[remainder_val]
    return converted_val[::-1]





def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    base_ten = decode(str_num, base1) #change base1 number to base 10
    converted_base = encode(base_ten, base2) #change base10 number to base2
    return converted_base


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        # print('Usage: {} number base1 base2'.format(sys.argv[0]))
        return "hello"


if __name__ == '__main__':
    main()
