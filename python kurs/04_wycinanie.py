# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:04:35 2024

@author: pogro
"""

name = "Python"

# %%
print(name)
print(name[0])
print(name[-1])

# %%
# name[start:stop]
# name[start:]
# name[:stop]
# name[start:stop:step]
name[1:4]
name[:4]
name[:]

# %%
name[-2:]
name[-3:-1]

# %%
full = 'Python Programming'
print(full[7:])
print(full[::2]) # co drugi znak

# %%
sample = '#stop#this#flow'
print(sample[::5])

# %%
numbers = '8,9,7,4'
print(numbers[::2])
print(numbers[::-1]) # od tyłu

# %%
name = 'kajak'
print(name[::-2])

# %%
name = 'Python'

'P' in name #testuje czy dany podciąg jest w naszym ciagu znaków TRUE/FALSE
'java' in name 


































