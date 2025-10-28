# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:51:30 2024

@author: pogro
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

def add(x, y):
    """Zwraca sume dwóch liczb.
    
    >>> add(3, 4)
    7
    
    >>> add(5,5)
    10

    """
    return x + y
    
if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')