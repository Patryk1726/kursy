# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:17:38 2024

@author: pogro
"""

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

# %%
name_google = google[0]
print(name_google)

# %% 
data = (google, amazon) #tupla zagnieżdżona
print(data)

# %%
a = ('Patryk', 'Ogrodowicz')
print(a)

# %%
imie = ('Patryk')
nazwisko = ('Ogrodowicz')

# %%
imie, nazwisko = ('Patryk', 'Ogrodowicz')

 # %%
 amazon_name, country, sector, rank = amazon #przypisanie kazdej zmiennej tego co w tupli amazon
 
 # %%
 stocs = 'Amazon', 'Apple', 'IBM' # nie trzeba dawac okraglego nawiasu
 print(type(stocs))
 
 # %%
 nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw') # tupla w tupli
 print(nested)
 
 # %%
 a = 12
 b = 14
 
 c = b
 b = a
 a = c

# %%
x, y = 10, 15
x, y = y, x
print(x, y) 
 
 
 
 
 
 
 
 
 
 
 
 