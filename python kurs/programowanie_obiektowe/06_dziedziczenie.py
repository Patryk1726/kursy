# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:27:34 2024

@author: pogro
"""

class Czlowiek:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
        
    def info(self):
        super().info()
        print(f'Klub {self.klub}')

# %%
pilkarz_1 = Pilkarz('Patryk', 'Ogrodowicz', 'Bayern')
pilkarz_2 = Pilkarz('Krzysztof', 'Piatek', 'AC Milan')

# %%
pilkarz_1.info()
