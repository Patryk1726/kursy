# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 00:23:59 2024

@author: pogro
"""
import sys

class Magazyn:
        
    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow
        
    def wyswietl_dostepne_produkty(self):
        print('Dostepne produkty:')
        for produkt in self.lista_produktow:
            print(produkt)
            
    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produkut: ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
            print(f'Produkt {self.nazwa_produktu} został dodany.')
        else:
            print(f'Produkt {self.nazwa_produktu} jest już na liscie.')
        
    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu: ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print(f'Produkt {self.nazwa_produktu} został/a usuniety/ta.')
        else:
            print(f'Produktu {self.nazwa_produktu} nie ma na liscie.')
            
magazyn = Magazyn(['mleko', 'woda', 'piwo', 'chleb', 'masło'])

while True:
    print('Wprowadź 1 aby wyswietlic stan magazynu.')
    print('Wprowadź 2 dodać produkt.')
    print('Wprowadź 3 aby usunac produkt.')
    print('Wprowadź 4 aby zakończyć.')
    wybor_uzytkownika = int(input('>>> '))
    
    if wybor_uzytkownika is 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika is 2:
        magazyn.dodaj_produkt()
    elif wybor_uzytkownika is 3:
        magazyn.usun_produkt()
    elif wybor_uzytkownika is 4:
        sys.exit()
    















