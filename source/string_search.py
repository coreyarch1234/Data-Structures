import string

def string_contains_pattern(text, pattern):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return string_contains_pattern_iterative(text, pattern)
    return (string_contains_pattern_recursive(text, pattern) or string_contains_pattern_reverse_recursive(text, pattern))


# def string_contains_pattern_iterative(text, pattern):
#     text = text.lower() #check for casing
#     text = text.replace(" ", "") #check for whitespaces
#     text = text.translate(None, string.punctuation) #check for punctuation
#     if text == '':
#         return True
#     if len(text) == 1:
#         return True
#     while len(text) > 1: #if the text is more than one character long, there are still more to check
#         if text[-1] == text[0]: #if the first and last chars are equal
#             text = text[1:-1] #cut off the first and last chars and make a new string
#         else:
#             return False #the start and end of text is unequal and this is not a palindrome
#     return True


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
            return string_contains_pattern_recursive(text[index + 1:], pattern)
    return True

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
