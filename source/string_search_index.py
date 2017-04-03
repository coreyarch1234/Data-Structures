import string

def string_contains_pattern_index(text, pattern):
    assert isinstance(text, str)
    return string_contains_pattern_index_recursive(text, pattern)
    # return string_contains_pattern_index_iterative(text, pattern)


def string_contains_pattern_index_iterative(text, pattern):
    for index in range(0, len(text) - len(pattern) + 1): #7
        length = len(pattern) + index # 5
        if text[index:length] == pattern:
            return index
    return None

def string_contains_pattern_index_recursive(text, pattern, count=0):
    counter = count
    if len(text) <= len(pattern):
        return counter
    for index in range(len(pattern)): #run through the length of the pattern
        if pattern == text[0:len(pattern)]: #if the respective letters of the text and pattern are equal, check the next
            return counter
        else: #if they are not equal, then run this method again with the text starting at the next letter.
            counter += 1
            return string_contains_pattern_index_recursive(text[index + 1:], pattern, count=counter)
    return None


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        print(string_contains_pattern_index('hel LLL !o', 'LL !'))

    else:
        print('hello')


if __name__ == '__main__':
    main()
