# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:16:05 2024

@author: pogro
"""

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

# %%
pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy':'three'}

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3}

# %%
name_to_digit = {0:1, 1:2, 2:3}

len(name_to_digit)

# %%
pol_to_eng['cztery'] = 'four' # przypisanie klucza i wartoci do słownika pol_to_eng

# %%
pol_to_eng.clear() #czyszczenie słownika

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %%
pol_to_eng.keys() # wydobywanie kluczy

# %%
list(pol_to_eng.keys()) # przekonwertowanie danych na liste z kluczami

# %%
pol_to_eng.values() # wydobywanie wartosci

# %%
list(pol_to_eng.values()) # przekonwertowanie danych na liste z wartociami

# %%
pol_to_eng.items() # wydobywanie klucza i wartosci

# %%
list(pol_to_eng.items()) # lista tupli

# %%
pol_to_eng['jeden'] 
#pol_to_eng['zero']

# %%
pol_to_eng.get('zero', 'NaN')

# %%
pol_to_eng.pop('dwa') # trzeba podać klucz albo wartoć

# %%
pol_to_eng.popitem() # nie trzeba podawać

# %%
pol_to_eng.update({'jeden':1}) # aktualizuje słownik

# %%
sorted(pol_to_eng) # sortuje alfabetycznie

















































