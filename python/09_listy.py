# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:01:13 2024

@author: pogro
"""

empty_list = list()
print(empty_list)

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7' # mozliwosc zmiany wartoci
print(techs)

# %%
numbers = [2, 3, 6, 45, 8]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.7, 4, True]
print(mixed)

# %%
pelna_lista = list([2, 'truskawka', True, 'tak'])
print(pelna_lista)
pelna_lista.append(6)
print(pelna_lista)

# %%
empty = []
nested = [['sql', 2, True],[3, 'kakao', 'babcia', False], 5]
print(nested)

# %%
first = ['mleko', 'makaron', 'maslo','banany']
second = ['piwo', 'wino', 'wódka']

oba = [first, second] # lista zagnieżdżona 
print(oba)
print('Iloć list:',len(oba))

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs += ['javascript']
print(techs)

# %%
print(dir(list)) # sprawdza dostepne metody dld konstruktora list

# %%
my_list = ['a', 'b', 'c', 'd']
my_list[:2] = ['x', 'y', 'z']
print(my_list)
 






















