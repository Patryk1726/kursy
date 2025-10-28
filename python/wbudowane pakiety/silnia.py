# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:20:56 2024

@author: pogro
"""

import sys

def silnia(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

if __name__ == '__main__': # gdy plik uruchamiany jest bezposrednio
    print(silnia(int(sys.argv[1])))