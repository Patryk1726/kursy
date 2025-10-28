# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:23:09 2024

@author: pogro
"""

print(abs(10))
print(abs(-10)) # zwraca wartosc bezwzgledna

# %%
bool([])  #False
bool('')  #False
bool({})  #False
bool(' ') #True
bool(True)
bool(False)
bool(0)  #False
bool(12) #True

# %%
dir() # zwraca wszywstkie atrybuty i metody obiektu
dir(list)
dir(tuple)

# %%
list(enumerate(['pawel', 'python','java'])) # lista tupli zawierające index na pierwszym miejscu

# %%
eval('1 + 1')
x = 10
eval('x + 13') #nie trzeba konwertowac na inty ytlko od razu oblica to co w stringu

# %%
print(list(filter(abs, [-2, -1, 0, 1, 2])))

list(filter(bool, ['python','','java']))

# %%
float(1) # liczba zmiennoprzecinkowa
float('1')
float('dfrf') #bład

# %%
type(1) # zwraca typ danego elementu (int, str)
type('erfg')

# %%
help(float) # sprawdzamy jak dziala funkcja

# %%
print(isinstance(1, int)) # bada czy dany obiekt jest instancja danej klasy
print(isinstance(1, float))
print(isinstance('', str))

# %%
len('python') #zwraca dlugosc danego elementu

# %%
list('python')
list(range(10))

# %%
list(map(abs, [-2, -1, 0, 1, 2])) # [2, 1, 0, 1, 2]

# %%
names = ['pawel', 'tomek', 'janek']
list(map(str.title, names))

# %%
max(1, 2, 3, 4, 7)
max('pawel') #zwroci litere alfabetycznie najdalej
max('tomek')
min(3, 5, 7, 2)
min('patryk') #zwroci litere alfabetycznie najdalej

# %%
pow(2, 4) #podnoszenie liczby do potęgi - 2 do 4
2 ** 4 # to samo

# %%
list(reversed([5, 6, 8, 3, 3])) # odwraca kolejnosc w obiekcie iterowalnym
list(reversed('sarthwrth'))

# %%
round(5.56565, 3) #zaokrąglenie do ilu miejsc po przecinku

# %%
str(4) # liczba na tekst

# %%
sum([3, 4, 6, 87]) # liczy sume obiektów

# %%
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

list(zip(lista_1, lista_2)) # łączy rownolegle elementy w tuple

# %%
list(zip('python', 'course'))


