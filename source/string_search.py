import string

def string_contains_pattern(text, pattern):
    assert isinstance(text, str)
    return string_contains_pattern_iterative(text, pattern) or string_contains_pattern_reverse_iterative(text, pattern)
    # return (string_contains_pattern_recursive(text, pattern) or string_contains_pattern_reverse_recursive(text, pattern))

def string_contains_pattern_iterative(text, pattern):
    #base case 1 - text and pattern are the same string
    if text == pattern:
        return True
    if len(text) < len(pattern):
        return False
    index = 0
    pattern_count = 1
    while len(text) >= len(pattern):
        # print(len(text))
        if pattern[index] == text[index]:
            if pattern_count == len(pattern):

                return True
            pattern_count += 1
            index += 1
        else:
            text = text[index + 1:]
            pattern_count = 0
            index = 0
        if pattern_count == len(pattern):
            return True
    return False

def string_contains_pattern_reverse_iterative(text, pattern):
    #base case 1 - text and pattern are the same string
    text = text[::-1] # reverse text
    pattern = pattern[::-1] #reverse pattern
    if text == pattern:
        return True
    if len(text) < len(pattern):
        return False
    index = 0
    pattern_count = 1
    while len(text) >= len(pattern):
        # print(len(text))
        if pattern[index] == text[index]:
            if pattern_count == len(pattern):
                return True
            pattern_count += 1
            index += 1
        else:
            text = text[index + 1:]
            pattern_count = 0
            index = 0
        if pattern_count == len(pattern):
            return True
    return False

def string_contains_pattern_recursive(text, pattern):
    #base case 1 - text and pattern are the same string
    if text == pattern:
        return True
    #base case 2 - the text pattern length is larger than the text, which means there is no way the text
    #contains the pattern
    if len(text) < len(pattern):
        return False
    for index in range(len(pattern)): #run through the length of the pattern
        if pattern[index] == text[index]: #if the respective letters of the text and pattern are equal, check the next
            continue
        else: #if they are not equal, then run this method again with the text starting at the next letter.
            return string_contains_pattern_recursive(text[index + 1:], pattern)
    return True

def string_contains_pattern_reverse_recursive(text, pattern): #Check for the reverse pattern. Check test line 35 for reference. (i.e. ('hel LLL !o', 'LL !') should be true the reverse way )
    #base case 1 - text and pattern are the same string
    text = text[::-1] # reverse text
    pattern = pattern[::-1] #reverse pattern
    if text == pattern:
        return True
    #base case 2 - the text pattern length is larger than the text, which means there is no way the text
    #contains the pattern
    if len(text) < len(pattern):
        return False
    for index in range(len(pattern)): #run through the length of the pattern
        if pattern[index] == text[index]: #if the respective letters of the text and pattern are equal, check the next
            continue
        else: #if they are not equal, then run this method again with the text starting at the next letter.
            return string_contains_pattern_reverse_recursive(text[index + 1:], pattern)
    return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        print(string_contains_pattern('fibbonaci', 'bbon'))

    else:
        print('hello')


if __name__ == '__main__':
    main()
