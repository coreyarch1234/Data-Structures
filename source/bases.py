#!python

import string
from math import *


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    universal_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #create list of characters that can be used
    universal_dict = {}
    count = 0
    for char in universal_list: #assign values to keys in dictionary
        universal_dict[char] = count
        count += 1
    num_by_base = reversed(list(str_num)) #reverse list to start from right to left
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
    assert 2 <= base <= 36
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
        converted_val += reverse_universal_dict[remainder_val] #append remainder  to string
    return converted_val[::-1] #return reversed string

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """

    base_ten = decode(str_num, base1) #change base1 number to base 10
    converted_base = encode(base_ten, base2) #change base10 number to base2
    return converted_base



def switch_num(str_num):
    start_index = 0
    str_num = list(str_num[::-1])
    while len(str_num) % 4 != 0:
        str_num.append("0")
    for index in range(len(str_num)):
        # print str_num[index]
        if str_num[index] == "1":
            # print("hello")
            start_index = index
            # print start_index
            break

    for updated_index in range(start_index + 1, len(str_num)): #switch from 0 to 1 to find two's complement
        if str_num[updated_index] == "1":
            # print "string = 1"
            # print str_num
            str_num[updated_index] = "0"
            # print str_num
            # print str_num[updated_index]
        elif str_num[updated_index] == "0":
            # print "string = 0"
            # print str_num
            str_num[updated_index] = "1"
            # print str_num

    return "1 1 1 1 " + " ".join(reversed(str_num))

def neg_convert(str_num, base1, base2): #Negative binary conversion
    """
    Convert given base 10 whether negative or positive to it's two's complemen tnumber from base1 to base2.
    """
    if int(str_num) == 0:
        return "0000"
    if int(str_num) > 0:
        base_ten = decode(str_num, base1) #change base1 number to base 10
        converted_base = encode(base_ten, base2) #change base10 number to base2
        return converted_base
    elif int(str_num) < 0:
        str_num_pos = str(int(str_num) * -1) #Make number positive
        base_ten = decode(str_num_pos, base1) #change base1 number to base 10
        converted_base = encode(base_ten, base2) #change base10 number to base2
        return switch_num(converted_base)






def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = neg_convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        # print('Usage: {} number base1 base2'.format(sys.argv[0]))
        str_num = args[0]
        result = switch_num(str_num)
        print(result)


if __name__ == '__main__':
    main()
