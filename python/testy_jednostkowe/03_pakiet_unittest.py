# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:39:39 2024

@author: pogro
"""

import unittest


def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3, 4), 7, 'Powinno być 7.')
        
        
if __name__ == '__main__':
    unittest.main()