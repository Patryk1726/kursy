# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:22:29 2024

@author: pogro
"""

def parabola(x):
    return x**2 + 3

print(type(parabola))
parabola(30)
# %%
funkcja_1 = parabola #przypisanie funkcji parabola do nowej zmiennej

funkcja_1(30)

# %%
f = lambda x: x**2 + 3
f(30) # tak samo działa jak funkcja wyżej - uzywamy do zdefiniowania funkcji w jednej linii

# %%
f_2 = lambda word: word.upper()
f_2('python')

# %%
add = lambda x, y: x + y
add(4, 7)

# %%
f_4 = lambda word_1, word_2: word_1 + ' ' + word_2
f_4('Hello', 'World')

# %%
lista = ['python', 'java', 'r', 'sql']

list(map(lambda word: word.upper(), lista)) # bierze funkcje lambda word: word.upper() i ją mapuje na liste

# %%
def make_upper(word):
    return word.upper()

list(map(make_upper, lista)) # to samo co wyżej tylko przy uzyciu funkcji def 

# %%
list(map(lambda word: word.title(), lista))

# %%
list(map(lambda word: (word, len(word)), lista))

# %%
def apply_function(x, fn):
    return fn(x)

apply_function(5, lambda x: x**2)
apply_function([23, 54], lambda x: sum(x)) # agregowanie danych

# %%
numbers = [6, 7, 3, 6, 3 ,7, 2]
sorted(numbers)
# wynik: [2, 3, 3, 6, 6, 7, 7]

numbers = [-3, -2, -1, 0, 1, 2, 3]
sorted(numbers, key= lambda x: abs(x)) # sortowanie po module liczby
# wynik: [0, -1, 1, -2, 2, -3, 3]

# %%
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy','three')]

sorted(lista) # sortowanie po kolejnosci literki w alfabecie

sorted(lista, key=lambda x: x[1]) # sortowanie po kolejnosci literki w alfabecie ale po drugim elemencie w tupli






















