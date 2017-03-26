#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    text = text.lower() #check for casing
    text = text.replace(" ", "") #check for whitespaces
    text = text.translate(None, string.punctuation) #check for punctuation
    if text == '':
        return True
    if len(text) == 1:
        return True
    while len(text) > 1: #if the text is more than one character long, there are still more to check
        if text[-1] == text[0]: #if the first and last chars are equal
            text = text[1:-1] #cut off the first and last chars and make a new string
        else:
            return False #the start and end of text is unequal and this is not a palindrome
    return True


def is_palindrome_recursive(text, left=None, right=None):
    #base case 1 - there is a blank string
    text = text.lower() #check for casing
    text = text.replace(" ", "") #check for whitespaces
    text = text.translate(None, string.punctuation) #check for punctuation
    if text == '':
        return True
    #base case 2 - the text is one char long
    if len(text) == 1:
        return True
    #recursive call. check start and end of text and if they are equal, check again and again until text is one character long
    #if text is of length one, text is a palindrome
    return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])


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
