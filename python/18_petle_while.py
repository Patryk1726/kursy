# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:42:15 2024

@author: pogro
"""

i = 0
while i < 5:
    print(i)
    i += 1
    
# %%
n = 0
while True:
    print(n)
    if n > 10:
        break
    n += 1

# %%
while True:
    name = input('Podaj sowje imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Czesc {}!'.format(name))

# %%
n = 0
while n < 20:
    n += 1
    if n % 2 == 1:
        continue
    print(n)

# %%
lista_do_przeszukania = [12, 54, 45 ,67, 43]
flaga = False

index = 0
while index < len(lista_do_przeszukania):
    print(lista_do_przeszukania[index])
    index += 1

# %%
lista_do_przeszukania = [12, 54, 45 ,67, 43]
flaga = False
wartosc = 67

index = 0
while index < len(lista_do_przeszukania):
    if lista_do_przeszukania[index] == wartosc:
        flaga = True
        break
    index += 1
if flaga:
    print('Znaleziono element {}.'.format(wartosc))
else:
    print('Nie ma szukanej wartoci.')
    
 # %%
 lista_do_przeszukania = [12, 54, 45 ,67, 43]
 flaga = False
 wartosc = 67

 index = 0
 while index < len(lista_do_przeszukania):
     if lista_do_przeszukania[index] == wartosc:
         flaga = True
         break
     index += 1
 if not flaga:
     print(lista_do_przeszukania.append(wartosc))

# %%
proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 150
}
calkowita_ilosc_gram = 3000
licznik = 0 
nowe_skladniki = {}

while licznik < calkowita_ilosc_gram:
    for skladnik, ilosc in proportions.items():
        if skladnik not in nowe_skladniki:
            nowe_skladniki[skladnik] = ilosc # jeżeli składnika nie ma w nowe_skladniki to ustawia bazową ilosc
        else:
            nowe_skladniki[skladnik] += ilosc
        licznik = licznik + ilosc
print('To prepare {} g of dough, you need:'.format(calkowita_ilosc_gram))
for skladnik, ilosc in nowe_skladniki.items():
    print(skladnik.capitalize(), '-',ilosc,'g')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


































