# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:25:18 2024

@author: pogro
"""

class A:
    
    def metoda(self):
        print('Metoda z klasy A.')

class B(A):
    
    def metoda(self):
        print('Metoda z klasy B.')
        
class C(A):
    
    def metoda(self):
        print('Metoda z klasy C.')
        
class D(B, C):
    
    def metoda(self):
        print('Metoda z klasy D.')
        
# %% 
d = D()
d.metoda()