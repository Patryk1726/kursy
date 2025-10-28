# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:13:42 2024

@author: pogro
"""

raw_data = '345!3456!345!3455'

for i in raw_data:
    if i == '!':
        continue
    print(i)
# %%
raw_data = '345!3456!345!3455'
clean = ''

for i in raw_data:
    if i != '!':
        clean += i
    else:
        clean += ','
print(clean)

# %%
suma = 0

for i in range(10):
    suma = suma + i
print(suma)

# %%
saldo = 450
print('Saldo początkowe {}.'.format(saldo))
for kwota in range(10, 60, 10):
    print('Wypłacona kwota:',kwota)
    saldo -= kwota
    print('Saldo :{}'.format(saldo))
print('Saldo końcowe:{}'.format(saldo))
 # %%
 print('Witaj w systemie logowania.')
 nick = input('Podaj nazwę: ')
 pin = input('Podaj pin, {}: '.format(nick))
 
 if len(pin) == 4:
     for char in pin:
         if char not in '0123456789':
             print('Podałes niepoprawny kod pin.')
             break
         else:
             print('Kod poprawny.')
             break
else:
    print('Niepoprawna długoć kodu pin.')

# %%
         
 




































