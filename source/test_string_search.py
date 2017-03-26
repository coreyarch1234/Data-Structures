from string_search import string_contains_pattern
import unittest

class TestStringSearch(unittest.TestCase):
    #these tests are for patterns that are in strings exactly the way they are written.

    def test_is_pattern_in_string(self):

        assert string_contains_pattern('hello', 'hell') is True
        assert string_contains_pattern('h', 'h') is True
        assert string_contains_pattern('', '') is True
        assert string_contains_pattern('fibbonaci', 'bbon') is True
        assert string_contains_pattern('oneloveoneworld', 'eloveon') is True

    def test_is_pattern_in_case_string(self):

        assert string_contains_pattern('helLO', 'lL') is True
        assert string_contains_pattern('ONEWORLDONELOVE', 'WORLD') is True
        assert string_contains_pattern('HelloMYnaMEisCoreyHarriLAL', 'lloMYn') is True

    def test_is_pattern_in_punctuation_string(self):

        assert string_contains_pattern('hel,!?', 'l,') is True
        assert string_contains_pattern('ONE?ORLDON.LO!E', 'DON.') is True
        assert string_contains_pattern('He.oMYnaMEis.....HarriLAL', 'is...') is True

    def test_is_pattern_in_whitespacing_string(self):

        assert string_contains_pattern('hel l o', 'hel') is True
        assert string_contains_pattern('fi bbo naci', 'fi bbo') is True
        assert string_contains_pattern('o nelove onewo rld', 'o') is True

    def test_is_pattern_in_case_punctuation_whitespacing_string(self):

        assert string_contains_pattern('hel LLL !o', 'LL !') is True
        assert string_contains_pattern('f i b!.?!.bo na  i', 'b!.') is True
        assert string_contains_pattern('o nel.! ? ve onewo rld', 'rld') is True

    def test_is_pattern_not_in_string(self):

        assert string_contains_pattern('hello', 'hell o') is False
        assert string_contains_pattern('fibbci', 'bbon') is False
        assert string_contains_pattern('onelovrld', 'elovd') is False



if __name__ == '__main__':
    unittest.main()
