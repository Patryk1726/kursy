# -*- coding: utf-8 -*-

imie = 'Jan'
wiek = 30
print(imie, wiek)

print('Czesc, ', end='') # okresla co zostanie wydrukowane na końcu ostatniej linii tekstu
print('swiecie')

print('Czesc','swiecie', sep='+')

with open('tekst.txt','w') as f:
    print('Czesc','swiecie', file=f)
    
# %%
print(2 + 2)

# %%
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 / 3
4 / 2

# %%
10 // 3
7 // 6

# %%
2 ** 5

# %% 
10 % 3
12 % 5

# %%
a = 10
b = 20
c = a * b
print(c)

# %%
print('love python')
"love python"

# %%
print("It's the best!")

# %%
print('It\'s the best!')

# %%
print("Python 3.7")

print("Python\n3.7")

print("""Python
3.7""")

# %%
print('\tPython')

# %%
print('C:\path\something\new') #błędne

print(r'C:\path\something\new') # r - surowy tekst
# %%
import os
os.getcwd() # scieżka dostępu do katalogu roboczego

# %%
print("""
Instrukcja uruchamiania pliku przykład.py:
          
    --file [nazwa pliku]
        zapisuje output do pliku
        
    --quiet
        wycisza logi w konsoli
        
Koniec.
      """)
# %%
text = 'I love python'
print(text)
print(text * 3)
print('kot..' * 3)

# %%
print("Python")
print("Py" "thon")

# %%
url = 'https://www.udemy.com/course/programowanie-w-jezyku-python/learn/lecture/15714542#content'

url2 = ('https://www.udemy.com/course/programowanie-w-jezyku-p'
'ython/learn/lecture/15714542#content')

# %% 
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

 # %%
age = 27
imie = 'Patryk'
print(imie, age)
print(imie + ' ' + str(age))
print('{} ma {} lat.'.format(imie, age))
print('{1} ma {0} lat.'.format(imie, age))

# %%
saldo = 40
saldo = saldo + 30     #saldo += 30
print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokatra_po_roku = lokata * czynnik_akumulacyjny
print('Wartoć lokaty po roku', lokatra_po_roku)
 # %%
 pixel = 150
 pixel = 150 / 255     #pixel /= 255
 print(pixel)

# %%
base = 2 
base = 2 ** 5     #base **= 5 
print(base)

# %%
x = 103
x = x % 10      # x %= 10
print(x)

# %%
imie = 'Patryk '
nazwisko = 'Ogrodowicz'
nazwa = imie + nazwisko
print(nazwa)

# %%
name = 'Python '
version =  '3.7'
name += version
print(name)



































