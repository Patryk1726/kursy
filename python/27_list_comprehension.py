# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:40:10 2024

@author: pogro
"""

results = []

for i in range(100):
    results.append(i ** 2)
print(results)

# %%
results_2 = [i**2 for i in range(100)]
print(results_2)

# %%
lista = [i * 3 for i in range(100)] # zamiast poniżej dodawac funkcje która cos tworzy tutaj przekazujemy ją najpierw

# %%
results = []

for i in range(100):
    if i % 5 == 0:
        results.append(i ** 2)
print(results)

# %%
results_2 = [i**2 for i in range(100) if i % 5 == 0] # to samo co wyżej tylko zapisane w jednej linii(list comprehension)

# %%
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

results = []
for letter in letters:
    for number in numbers:
        results.append(letter + str(number))

# %%
results_2 =[letter + str(number) for letter in letters for number in numbers]
        
# %%
letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']

results = [i + j for i in letters_1 for j in letters_2 if i != j]

# %%
[[j for j in range(10)] for i in range(10)]

# %%
[[(i, j) for j in range(10)] for i in range(3)]

# %%
[[(i * j) for j in range(10)] for i in range(3)]

# %%
[[l1 + l2 for l2 in 'abcdef'] for l1 in '12345']

# %%
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

[silnia(i) for i in range(5)] # zwraca kolejne wartoci silni (do 5 bo range(5))




























    