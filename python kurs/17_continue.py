# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:44:56 2024

@author: pogro
"""

for i in range(10):
    if i == 6:
        continue # pominięcie (przejcie do następnej iteracji)
    print(i)

# %%
for i in range(20):
    if i % 2 ==0:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 ==1: 
        continue
    print(i)

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
hashtag = '#summer#holiday#free'
result = '1'

for char in hashtag:
    if char == '#':
        print(result)
        result = '2'
        continue #jeżeli w warnuku jest prawda kod po continue nie zostanie wykonany i przechodzi do nastepnego znaku
    result = result + char
print(result)
 # %%
 numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    