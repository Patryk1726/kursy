# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:49:39 2024

@author: pogro
"""


text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'
print(text)

# %%
dir(text)
help(str.count) # pomoc i krótki opis jak działa funkcja

# %%
text.capitalize()

# %%
text.title()

# %%
text.count('Python')

# %%
print(text.startswith('Wi'))
print(text.startswith("kurs"))

# %%
'python'.startswith('pyt')

# %%
text.endswith('y.')

# %%
'sample.py'.endswith('.py')

# %%
'sample.png'.endswith('.png')

# %%
print(text.find('Python')) # zwraca indeks od którego zaczyna się wyszukiwany wyraz
print(text[text.find('Python'):])

# %%
hashtag = 'sport#gym'
index = hashtag.find('#')
print(hashtag[:index])

# %%
'pawel23'.isalnum() # znaki alfanumeryczne(czy są literą albo cyfrą)

# %%
'43234'.isdigit() # sprawdza czy wszysatkie znaki są cyframi

# %%
'python'.islower() # sporawdza czy wszystkie znaki są z małej litery

# %%
'PAWEL'.isupper() # sprawdza czy wszystkie są z dużej litery

# %%
print(' '.join(['python', '3.7'])) # łączenie ze sobą
print('#'.join(['Patryk', 'OG']))
print(','.join(['1', '2', '3', '4']))
    
# %%
words = ['bmw', 'audi', 'toyota', 'volkswagen', 'mercedes']
joined_words = '#'.join(words)
print(joined_words)

# %%
'#good#time#mood'.replace('#', ' ') # zastąpienie znaku innym 

# %%
'column name'.replace(' ', '_')

# %%
'   python   '.strip() # wycinanie spacji
'   python   '.rstrip() # wycinanie spacji po prawej stronie
'   python   '.lstrip() # wycinanie spacji po lewej stronie
# %%
# podzielenie wartosci tekstowych z wskazaniem znaku podziału(tym który już jest)
# obiekt zwraca liste (strukture danych)
print('1,2,3,4,5'.split(','))

print('python java php sql sas'.split(' '))

'#gym#power#fit#mood'.split('#')

# %%
'12'.zfill(5) # szerokoć ciagu znaków

'1'.zfill(12)






















































