# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:45:23 2024

@author: pogro
"""

def funkcja_1():
    print('Pierwsza funkcja uruchomiona.')
    
funkcja_1()

# %%
def funkcja_2(x, y):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funkcja_2(2, 6)

# %%
import math

math.sqrt(9) # pierwiastkowanie
math.exp(1)
math.sin(0)

# %%
def funkcja_3():
    print('Uruchomiono.')
    
funkcja_3()
print(type(funkcja_3))

# %%
def add(x, y):
    return x + y

add(2, 6)

# %%
def substract(x: int, y: int): # mozemy po dwukropku przekazac klase wartosci
    return x - y

substract(10, 6)

# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
          0 - logowanie
          1 - wyjscie""")
    print('*' * 30)
    print('Koniec programu.')
    
print_menu()

# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1): # +1 zmienia tutaj to żeby liczba którą wpiszemy np.10 była równiez brana pod uwage
        if i % 2 == 0:
            even.append(i)
    return even
print_even(10)
num = print_even(20)
    
# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)

write_file('sample.txt', 'Pierwsza linia.\nDruga linia.')

# %%
def calculate_profit(pv, rate,n):
    return pv *(1+rate)**n - pv
    
calculate_profit(10000, 0.2, 15)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
