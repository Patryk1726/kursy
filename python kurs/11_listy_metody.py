# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:36:41 2024

@author: pogro
"""

techs = []
print(techs)

# %%
techs.append('python')
print(techs)

#%%
techs.append('java')
print(techs)

# %%
techs.append(['hadoop', 'spark']) # dodaje liste zagnieżdźoną
print(techs) 

# %%
techs.extend(['sql', 'sas']) # dodaje do listy bez zagnieżdżenia
print(techs)

# %%
techs.insert(0,'go') # wstawia w odpowiednie miejsce po podaniu indexu
print(techs)

# %%
techs.insert(2, 'r')
print(techs)

# %%
techs.pop() # usuwa ostatni element
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php']
print(techs.pop(0)) #usuwa z listy wartoć pod indexem 0
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php']
print(techs.index('java')) #dos tajemy numer indexu jezeli wartoć podana jest w liscie

# %%
techs = ['python', 'java', 'sql', 'php', 'python']
print(techs.count('python')) # zlicza ilosć 

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort() #sortuje alfabetycznie
#techs.sort(reverse=True) #sortuje alfabetycznie odwrotnie
print(techs)

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
#print(techs[::-1]) # tak samo odwraca liste
techs.reverse() # tak samo odwraca liste
print(techs)

 # %%
 techs[1] = 'c++' # podmianka
 print(techs)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 






























