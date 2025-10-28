# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:34:15 2024

@author: pogro
"""

saldo = 10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany:
    print('Możesz wypłacić gotówke.')
else:
    print('Nie możesz wypłacić gotówki.')
    
# %%

saldo = 10000
klient_zweryfikowany = True
kwota =  int(input('Podaj ile chesz wypłacić:'))

if saldo > 0 and klient_zweryfikowany and kwota < saldo:
    print('Możesz wypłacić gotówke.')
else:
    print('Nie możesz wypłacić gotówki. '
          'Brak wystarczającej kwoty {}.'.format(abs(saldo - kwota))) 

# %%

name = 'python'

if 'p' in name:
    print('Znaleziono p.')
else:
    print('Nie znaleziono p.')

# %%

tech = 'python'
if tech == 'python':
    flag = 'Dobry wybór.'
else:
     flag = 'Poszukaj czego lepszego.'

# %%
#x if [warunek] else y
tech = 'python'
'Dobry wybór' if tech == 'python' else 'Poszukaj czego lepszego.'

# %%































