# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:09:52 2025

@author: pogro
"""

def fib(n):

    a, b = 0, 1
    result = [a]
    for i in range(n - 1):
        a, b = b, a + b
        result.append(a)
    return result
        
n = 10
print(fib(n))