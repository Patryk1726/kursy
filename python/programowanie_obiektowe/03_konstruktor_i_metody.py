# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:30:12 2024

@author: pogro
"""

class Drzewo: # tu tworzymy klase
    
    def __init__(self, nazwa, wiek, wysokosc): #to jest metoda
        self.nazwa = nazwa # tu są atrybuty zdefiniowane w metodzie
        self.wiek = wiek
        self.wysokosc = wysokosc
        
        
    def czy_chronione(self):
        if self.wiek >= 20 and self.wysokosc >= 20:
            print(f'Drzewo o nazwie {self.nazwa} i wysokosci {self.wysokosc} jest pod ochroną.')
        else:
            print(f'Drzewo o nazwie {self.nazwa} nie jest pod ochroną.')
            
    def postarz_o_rok(self):
        self.wiek += 1
# %%
drzewo_1 = Drzewo('Sosna', 35, 25) # tu tworzymy obiekt/instancje klasy - drzewo_1
drzewo_2 = Drzewo('Brzoza', 18, 40)

# %%
print(drzewo_1.nazwa) 
print(drzewo_2.nazwa)

# %%
drzewo_1.czy_chronione() # wywołanie metody dla obiektu drzewo_1
drzewo_2.czy_chronione()
# %%

drzewo_1.postarz_o_rok()
print(drzewo_1.wiek)