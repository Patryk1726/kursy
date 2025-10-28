# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:48:34 2024

@author: pogro
"""

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Jacek'
    
class Polak:
    
    kraj = 'Polska'
    imie = 'Piotrek'
    
class Pilkarz(Polak, Czlowiek):
    
    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\nKraj pochodzenia {self.kraj}.'
              f'\nNazwa obiektu: {self.imie}')
        
# %%
pilkarz_1 = Pilkarz()
pilkarz_1.info()