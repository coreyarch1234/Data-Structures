from hashset import HashSet
import unittest


class HashSetTest(unittest.TestCase):

    def d_test_init(self):
        hs = HashSet("A")
        assert len(hs.buckets) == 8
        assert hs.size == 1

    def d_test_size(self):
        hs = HashSet(["A", "B", "XYZ", "4"])
        assert hs.size == 4
        hs_two = HashSet()
        assert hs_two.size == 0

    def d_test_contains(self):
        hs = HashSet(["A", "B", "XYZ", "4"])
        assert hs.contains("B") == True
        assert hs.contains("XYZ4") == False
        assert hs.contains("") == False


    def test_add(self):
        hs = HashSet([1, 3, 5, 7]) # size 4
        assert hs.contains(23) == False
        hs.add(23) #size 5
        assert hs.contains(23) == True
        hs.add(2) #size 6
        assert hs.size == 6


    def d_test_contains(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.contains('I') is True
        assert ht.contains('V') is True
        assert ht.contains('X') is True
        assert ht.contains('A') is False

    def d_test_set_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3
        assert ht.size == 3
        with self.assertRaises(KeyError):
            ht.get('A')  # Key does not exist

    def d_test_set_twice_and_get(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 4)
        ht.set('X', 9)
        assert ht.length() == 3
        assert ht.size == 3
        ht.set('V', 5)  # Update value
        ht.set('X', 10)  # Update value
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.length() == 3  # Check length is not overcounting
        assert ht.size == 3  # Check size is not overcounting

    def d_test_delete(self):
        ht = HashTable()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.length() == 3
        assert ht.size == 3
        ht.delete('I')
        ht.delete('X')
        assert ht.length() == 1
        assert ht.size == 1
        with self.assertRaises(KeyError):
            ht.delete('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            ht.delete('A')  # Key does not exist

    def d_test_keys(self):
        ht = HashTable()
        assert ht.keys() == []
        ht.set('I', 1)
        assert ht.keys() == ['I']
        ht.set('V', 5)
        self.assertItemsEqual(ht.keys(), ['I', 'V'])  # Ignore item order
        ht.set('X', 10)
        self.assertItemsEqual(ht.keys(), ['I', 'V', 'X'])  # Ignore item order

    def d_test_values(self):
        ht = HashTable()
        assert ht.values() == []
        ht.set('I', 1)
        assert ht.values() == [1]
        ht.set('V', 5)
        self.assertItemsEqual(ht.values(), [1, 5])  # Ignore item order
        ht.set('X', 10)
        self.assertItemsEqual(ht.values(), [1, 5, 10])  # Ignore item order

    def d_test_items(self):
        ht = HashTable()
        assert ht.items() == []
        ht.set('I', 1)
        assert ht.items() == [('I', 1)]
        ht.set('V', 5)
        self.assertItemsEqual(ht.items(), [('I', 1), ('V', 5)])
        ht.set('X', 10)
        self.assertItemsEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])


if __name__ == '__main__':
    unittest.main()
