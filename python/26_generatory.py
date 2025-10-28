# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:13:15 2024

@author: pogro
"""

def generator():
    
    yield 4
    
    yield 5
    
# %%
gen = generator()

# %%
next(gen)

# %%
def generator_2(word):
    letters = list(word)
    for letter in letters:
        yield letter
        
gen2 = generator_2('python')
# %%
next(gen2)

# %%
for i in generator_2('predator'):
    print(i)
    
# %%
files = ['script_1.py', 'script_2.py', 'text.py']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = gen_files(files)
        
# %%
next(gen)

# %%
for i in gen:
    print(i)
# %%
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
        
fib = fibonacci()
# %%
print(next(fib))

# %%
def geometric_sequence(a, b):
    while True:
        yield a 
        a = a * b
geo = geometric_sequence(2, 100)

# %%
print(next(geo))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        