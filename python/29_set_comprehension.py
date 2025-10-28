# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:59:48 2024

@author: pogro
"""
# %%
text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.','').split()

unique_words = {word for word in words}
print(unique_words)

# %%
unique_words_4 = {word for word in words if len(word) > 4}
print(unique_words_4)

# %%
{word.capitalize() for word in words if word.startswith('pyt')}