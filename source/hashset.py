
from linkedlist import LinkedList


#Set implemented as a hashtable
class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash table with the given initial size"""
        # init_size=8 implement hash table instance
        self.buckets = [LinkedList() for i in range(8)]
        self.size = 0  # Count number of key-value entries
        if elements:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets"""
        # TODO: Calculate load factor
        num_buckets = float(len(self.buckets))
        return float(self.size) / num_buckets # l = n/b, where n is the number of key value entries

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)."""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = self.size * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = self.size / 2  # Half size
        # TODO: Get a list to temporarily hold all current key-value entries
        temp_list = self.items() #returns the list of key-value entries in hash table
        # ...
        # TODO: Create a new list of new_size total empty linked list buckets
        new_size_list = [LinkedList() for i in range(new_size)] #new sized linked list bucket
        self.buckets = new_size_list
        self.size = 0
        # ...
        # TODO: Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in temp_list:
            self.set(key,value) #rehashes keys and inserts them in new buckets according to new size
        # ...

    def contains(self, element):
        """Return True if this hash table contains the given key, or False"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda (k, v): k == element)
        return entry is not None  # True or False

    def add(self, element): #add key of set element and value of unit type - 1
        """Insert or update the given key with its associated value""" #with hash instance
        unit_type = 1 #dummy value
        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda (k, v): k == element)
        if entry is not None:  # Found
            #In this case, we don't want to do anything
            return
        # Insert the new key-value entry into the bucket in either case
        bucket.append((element, unit_type))
        self.size += 1
        if self.load_factor() > 0.75:
            self._resize()

    def remove(self, element): #remove element from set if it exists
        """Delete the given key and its associated value, or raise KeyError"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda (k, v): k == element)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise ValueError('Element not found: {}'.format(element))

    def union(self, second_set): #Assume the second set is of type, HashSet
        """Return the union of the current set and the second set, don't update this set"""
        union_set = HashSet() #union set to be filled
        for element in second_set.keys():
            union_set.add(element) #adds second set elements into union
        for element in self.keys():
            union_set.add(element) #adds current set elements into union
        return union_set

    def intersection(self, second_set): #Assume the second set is of type, HashSet
        """Return the intersection of the current set and the second set, don't update this set"""
        intersection_set = HashSet() #union set to be filled
        for element in self.keys():
            if element in second_set.keys(): #if they have the same element
                intersection_set.add(element)
        return intersection_set

    def difference(self, second_set): #Assume the second set is of type, HashSet
        """Return the difference of the current set and the second set, don't update this set difference
        of A and B is the elements in B that are not in A"""
        difference_set = HashSet() #union set to be filled
        for element in second_set.keys():
            if element not in self.keys(): #if they have the same element
                difference_set.add(element)
        return difference_set

    def is_subset(self, second_set): #Assume the second set is of type, HashSet
        """Return True if second_set if a subset of current set. False otherwise."""
        for element in second_set.keys():
            if element not in self.keys(): #if they have the same element
                return False
        return True


    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys


    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items


def test_hash_table():
    h_one = HashSet(["A", "B", "C", "1"])
    h_two = HashSet(["A", "B"])
    print(h_one.is_subset(h_two))

if __name__ == '__main__':
    test_hash_table()
