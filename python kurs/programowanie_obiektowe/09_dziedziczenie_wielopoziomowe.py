# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:31:11 2024

@author: pogro
"""

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Jack'
    
class Polak(Czlowiek):
    
    kraj = 'Polska'
    imie = 'Kuba'
    
class Programista(Polak):
    
    technologia = 'Python'
    imie = 'Patryk'
    
    def info(self):
        print(f'Pochodzenie: {self.pochodzenie}\n'
              f'Kraj: {self.kraj}\n'
              f'Stosowana technologia: {self.technologia}\n'
              f'Imie: {self.imie}')
        
# %%
programista_1 = Programista()
programista_1.info()