# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:27:07 2024

@author: pogro
"""

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++','sql'}
print(techs)
print(type(techs))
print(len(techs)) # zwraca długosc zbioru

# %%
print(set('python'))
set('aaaaaaaale')

# %%
'python' in techs
'go' in techs

# %%
print(dir(set)) #sprawdz dostępne metody dla konstruktora set

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sas')
print(techs)

# %%
techs.pop() # wywala ze zbioru dowolny losowy element

# %%
techs.clear() # wyczyci cały zbiór
print(techs)

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8 ,9}
C = {5, 6}

print(C.issubset(A)) # sprawdza czy dane ze zbioru C są w zbiorze A
print(C.issubset({5, 7}))
print(A.issuperset(C)) # sprawdza czy A jest nadzbiorem 
#(sprawdza czy zbiór C posiada wszystkie te same elementy co zbiór A)

print(A.union(B)) # suma zbioru A i B (te same elementy zbioru nie powtarzają się)
print(A.intersection(B)) # zwraca wspólne wartosci z obu zbiorów
print(A.symmetric_difference(B)) # elementy które są w zbiorze A ale nie są w zbiorze B i na odwrót
D = A.copy() # kopiuje zbiów A

# %% 
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])
 
union_set = set(list(set1) + list(set2))
 
print('Union set without duplicates:', union_set)
 #%%
# moje rozwiązanie 
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

polaczenie = set1.union(set2)
print('Union set without duplicates:', polaczenie)


















