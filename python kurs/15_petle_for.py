# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:22:29 2024

@author: pogro
"""

for i in 'python':
    print(i)

# %%
name = 'sas'

for character in name:
    print(character)
    
# %%
name = 'python' # to samo
index = 0

for character in name:
    print(index, character)
    index = index + 1
# %%
for index in range(10):
    print(index)

# %%
for index in range(len(name)):
    print('Numer indexu:', index,'Litera:', name[index])

# %%
for i in enumerate(name):
    print(i)
    
# %%
for indeks, character in enumerate(name):
    print(indeks, character)

# %%
for i in [4, 5, 6, 7, 8]:
    print(i)

# %%
for i, value in enumerate([4, 5, 6, 7, 8]):
    print(i, value)

# %%
for i in range(10):
    print(i)

# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, 20, 2):
    print(i)

# %%
for i in range(10, 0, -1):
    print(i)

# %% 
techs = 'java' # to samo
for i in range(len(techs)):
    print(i, techs[i])
# %%
for i, name in enumerate('java'): # to samo
    print(i, name)

# %%
string = 'Python Course'
for char in string[:6]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
for char, number  in zip('abcde', '12345'):
    print(char, number)

# %%
hashtags = '#sport#gym#fitness#'
result = ''
for char in hashtags:   # in to =
    if char not in '#': # sprawdzamy czy nasz znak nie jest równy '#'
        result = result + char # jeżeli znak to nie # to dodajemy znak który jest normalny
    else:
        print(result) # jeżeli znak jest równy '#' to wyprintuje i zastąpi go result = '' czyli niczym 
        result = ''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    