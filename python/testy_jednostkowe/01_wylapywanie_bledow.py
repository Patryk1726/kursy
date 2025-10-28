# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:20:24 2024

@author: pogro
"""
# %%
1 / 0

# %%
4 + '4'

# %%
int('e')

# %%
float('gr')

# %%
try:
    1 / 0
except:
    print('Nie dzieli sie przez 0.')
# %%
try:
    1 / 0
except ZeroDivisionError:
    print('Nie dzieli sie przez zero!')
except TypeError:
    print('Zły typ.')

# %%
try:
    4 + '4'
except:
    print('Nie można dodawać tkstu do liczby.')
# %%
try:
    int('f')
except:
    print('Zły tekst.')
    
# %%
while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('Nie wprowadzono poprawnie liczby.')
        
# %%
try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('Nie znaleziono pliku.')
    
# %%
raise TypeError('Błąd.')

# %%
raise TypeError('Błąd wartosci.')

# %%

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Nie możesz wpisać zero!')
    except TypeError:
        print('Nie możesz używać stringa!')
    
    
    
divide(3, 0)
divide(3, '4')
    





































