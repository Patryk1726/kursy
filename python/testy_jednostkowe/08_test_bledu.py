# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:33:56 2024

@author: pogro
"""

import unittest

def div(a, b):
    return a / b

class RaiseTest(unittest.TestCase):
    
    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
        
if __name__ =='__main__':
    unittest.main()