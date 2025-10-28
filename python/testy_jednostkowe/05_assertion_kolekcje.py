# -*- coding: utf-8 -*-
"""
assertListEqual - sprawdza czy dwie listy są równe
assertTupleEqual - sprawdza czy dwie tuple sa równe
assertSetEqual - sprawdza czy dwa zbiory są równe
assertDictEqual - sprawdza czy dwa słowniki są równe
"""

import unittest

class SimpleTest(unittest.TestCase):
    
    def test_list_equal(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        
    def test_tuple_equal(self):
        self.assertTupleEqual((4, 5), (4, 5))
        
    def test_set_equal(self):
        self.assertSetEqual({7, 8, 9}, {7, 8, 9})
        
    def test_dict_equal(self):
        self.assertDictEqual({'a':'adam'},{'a':'adam'})
        
    
if __name__ == '__main__':
    unittest.main()
