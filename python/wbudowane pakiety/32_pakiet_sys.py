# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:56:26 2024

@author: pogro
"""

import sys 

sys.argv # zwraca liste przedstawiajaca nazwe pliku który uruchamiamy i argumenty które przekazujemy do tego pliku

print(sys.argv)

args = sys.argv

print('Nazwa pliku:', args.pop(0))

i = 1

while args:
    print('Argument numer {}: {}'.format(i, args.pop(0)))
    i+= 1