# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:38:22 2024

@author: pogro
"""

# public: zmienna
# protected: zmienna
# private: zmienna
# %%
class Spolka:
    
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda
        
class KGHM(Spolka):
    
    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrybut publiczny: {self.rodzaj}')
        print(f'Atrybut chroniony: {self._rynek}')
              # f'Atrybut prywatny {self.__gielda}'
# %%
spolka = Spolka('Spólka akcyjna', 'Główny', 'GPW w Warszawie')

print(f'Atrybut publiczny {spolka.rodzaj}')
print(f'Atrybut chroniony {spolka._rynek}')
# print(f'Atrybut prywatny {spolka.__gielda}')

# %%
kghm = KGHM('Spólka akcyjna', 'Główny', 'GPW w Warszawie', 'KGHM')
print(f'Atrybut prywatny: {kghm._Spolka__gielda}')