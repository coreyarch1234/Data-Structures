from string_search_index import string_contains_pattern_index
import unittest

class TestStringSearch(unittest.TestCase):
    #these tests are for patterns that are in strings exactly the way they are written.

    def test_is_pattern_in_string(self):

        assert string_contains_pattern_index('hello', 'hell') is 0
        assert string_contains_pattern_index('h', 'h') is 0
        assert string_contains_pattern_index('', '') is 0
        assert string_contains_pattern_index('fibbonaci', 'bbon') is 2
        assert string_contains_pattern_index('oneloveoneworld', 'eloveon') is 2

    def test_is_pattern_in_case_string(self):

        assert string_contains_pattern_index('helLO', 'lL') is 2
        assert string_contains_pattern_index('ONEWORLDONELOVE', 'WORLD') is 3
        assert string_contains_pattern_index('HelloMYnaMEisCoreyHarriLAL', 'lloMYn') is 2

    def test_is_pattern_in_punctuation_string(self):

        assert string_contains_pattern_index('hel,!?', 'l,') is 2
        assert string_contains_pattern_index('ONE?ORLDON.LO!E', 'DON.') is 7
        assert string_contains_pattern_index('He.oMYnaMEis.....HarriLAL', 'is...') is 10

    def test_is_pattern_in_whitespacing_string(self):

        assert string_contains_pattern_index('hel l o', 'hel') is 0
        assert string_contains_pattern_index('fi bbo naci', 'fi bbo') is 0
        assert string_contains_pattern_index('o nelove onewo rld', 'o') is 0

    def test_is_pattern_in_case_punctuation_whitespacing_string(self):

        assert string_contains_pattern_index('hel LLL !o', 'LL !') is 5 #Mirror Case
        assert string_contains_pattern_index('f i b!.?!.bo na  i', 'b!.') is 4
        assert string_contains_pattern_index('o nel.! ? ve onewo rld', 'rld') is 19


if __name__ == '__main__':
    unittest.main()
