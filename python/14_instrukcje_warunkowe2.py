# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:54:21 2024

@author: pogro
"""

print('Program uruchomiony...')
print("""Włam sie do systemu, zgadujac dwucyfrowy kod pin.
      Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin:')

if pin == '21':
    print('Brawo złamałes system.')
elif pin == '20':
    print('Byłes blisko.')
else:
    print('Nie zgadles.')

# %%
pin = int(input('Wprowadź numer pin:'))

if pin == 21:
    print('Brawo złamałes system.')
elif pin == 20:
    print('Byłes blisko.')
else:
    print('Nie zgadles.')
    
# %%
bool('')

# %%
string = ''
if string:
    print('Niepusty ciąg znaków.')
else:
    print('Pusty ciąg znaków.') # bo bool('') daje False

# %%
number = 1
if number:
    print('Liczba niezerowa.')
else:
    print('Zero!') # bo bool(0) daje False

# %%
default_flag = True

if default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło do defaultu.')

# %%
default_flag = False

if default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło do defaultu.')
    
# %%
default_flag = True

if  not default_flag == True:
    print('Nie doszło do defaultu.')
    
else:
    print('Doszło do defaultu.') 

# %%
default_flag = False

if not default_flag:
    print('Nie doszło do defaultu.')
    
else:
    print('Doszło do defaultu.') 
# %%
chuj = True

if not chuj:
    print('Nie jest chujem.')
else:
    print('Jest chujem.')

# %%
chuj = False

if not chuj:
    print('Nie jest chujem.')
else:
    print('Jest chujem.')







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    