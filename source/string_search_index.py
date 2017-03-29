import string

def string_contains_pattern_index(text, pattern):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return string_contains_pattern_iterative_index(text, pattern)

def string_contains_pattern_iterative_reverse_index(text, pattern):
    #base case 1 - text and pattern are the same string
    text = text[::-1] # reverse text
    pattern = pattern[::-1] #reverse pattern
    temp_text_count = 0
    if text == pattern:
        return 0
    if len(text) < len(pattern):
        return False
    index = 0
    pattern_count = 0
    while len(text) >= len(pattern):
        temp_text_count += 1
        if pattern[index] == text[index]:
            if pattern_count == len(pattern):
                return temp_text_count - len(pattern)
            pattern_count += 1
            index += 1
        else:

            text = text[index + 1:]
            index = 0
            if pattern[index] == text[index]:
                pattern_count = 0
            else:
                pattern_count = 1
        if pattern_count == len(pattern):

            # temp_text_count += 1
            return temp_text_count - len(pattern)
    return False

def string_contains_pattern_iterative_index(text, pattern):
    #base case 1 - text and pattern are the same string
    temp_text_count = 0
    if text == pattern:
        return 0
    if len(text) < len(pattern):
        return False
    index = 0
    pattern_count = 0
    while len(text) >= len(pattern):
        temp_text_count += 1
        # print(temp_text_count)
        if pattern[index] == text[index]:
            if pattern_count == len(pattern):
                return temp_text_count - len(pattern)
            pattern_count += 1
            index += 1
        else:
            
            text = text[index + 1:]
            index = 0
            if pattern[index] == text[index]:
                pattern_count = 1
            else:
                pattern_count = 0
        # print(pattern_count)
        if pattern_count == len(pattern):
            # temp_text_count += 1
            print("weird")
            return temp_text_count - len(pattern)
    if string_contains_pattern_iterative_reverse_index(text, pattern) == False:
        return False
    else:
        # print("weird")
        return string_contains_pattern_iterative_reverse_index(text, pattern)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        print(string_contains_pattern_index('f i b!.?!.bo na  i', 'b!.'))

    else:
        print('hello')


if __name__ == '__main__':
    main()
