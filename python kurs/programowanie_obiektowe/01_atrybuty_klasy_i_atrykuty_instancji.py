# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:11:33 2024

@author: pogro
"""

class Drzewo:
    
    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25
    
drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
print(id(drzewo_1)) # sprawdzanie id
print(id(drzewo_2))

# %%
print(dir(drzewo_1)) # atrybuty 

# %%
print(drzewo_1.nazwa)
print(drzewo_1.wiek)
print(drzewo_1.wysokosc)

# %%
drzewo_1.stan = 'dobry'
print(dir(drzewo_1)) # tu jest dodany stan
print(dir(drzewo_2)) # a tu nie

# %%
Drzewo.miejsce = 'las' # do kazdego obiektu sie przypisze

print(dir(drzewo_1))

# %%
drzewo_2.miejsce = 'park'

print(drzewo_2.miejsce)

































