# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:31:32 2024

@author: pogro
"""

import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y


class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.skipTest('pomiń')
        self.assertEqual(add(4, 5), 9)
        
    @unittest.skip('pomiń') # też pomija 
    def test_dub(self):
        self.assertEqual(sub(10, 5), 5)
        
        
if __name__ == '__main__':
    unittest.main()