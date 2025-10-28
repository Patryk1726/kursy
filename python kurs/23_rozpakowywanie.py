# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:27:30 2024

@author: pogro
"""

def test_args(x, *args):
    print('Pierwszy paramter:', x)
    for arg in args:
        print('Kolejny parametr *args:', arg)
        
test_args(4, 3, 4 ,45)

# %%
def funkcja_1(x, y, *args):
    print('x=', x)
    print('y=', y)
    print('*args=', args)

funkcja_1(2,4,7,7,6)

# %%
def suma(x, y):
    return x+ y

def suma_dowol(*args):
    return sum(args)

# %%
suma(1, 2)
suma_dowol(3, 56, 7, 6 ,8 ,4)

# %%
def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

funkcja_2(**{'a': 1, 'b': 2}) # otrzymujemy key

# %%
def fun(**kwargs):
    print(kwargs)

fun(x1=10, x2=20, x3=30) #otzymujemy słownik z argumentami(key: value)

# %%
def fun_2(*args, **kwargs): # **kwargs - argumenty ze zdefiniowaną nazwą
    print(args)
    print(kwargs)

fun_2(1, 2, 3, a=10, b=12)

# %%
def fun_3(*args, **kwargs):
    print(sum(args))
    print(sum(kwargs.values()))

fun_3(10, 54, 2, a=4, b=77)





























