# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:46:21 2024

@author: pogro
"""

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
    
    @staticmethod
    def liczba_studentow():
        print(len(Student.lista_studentow))
        
# %%
student_1 = Student('Patryk', 'Ogrodowicz', 22)
student_2 = Student('Tomasz', 'Nowak', 34)
student_3 = Student('Jan', 'Kowalski', 19)

# %%
Student.liczba_studentow()
