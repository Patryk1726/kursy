# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:41:47 2024

@author: pogro
"""

stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}
# %%
stocks.keys()
stocks.values()
stocks.items()

for key, value in stocks.items():
    print('{}: {}'.format(key, value))

# %%
stocks_dict = {key:value for (key, value) in stocks.items()}
print(stocks_dict)

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()} # zbiór elementów

# %%
stocks_invert = {value:key for (key, value) in stocks.items()} # odwrócony

# %%
stocks_lower = {key.lower():value for (key, value) in stocks.items()}

# %%
stocks_len = {key:len(value) for (key, value) in stocks.items()}

# %%
stocks_len = {key: mvalue + ':' + str(len(value)) for (key, value) in stocks.items()}

# %%
def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace('Inc', '1')
    return name

stocks_flag = {key:replace_corp_inc(value) for (key, value) in stocks.items()}

# %%
stocks_corp = {key:value for (key, value) in stocks.items() if 'Corp' in value}

# %%
stocks_A = {key:value for (key, value) in stocks.items() if value.startswith('A') and len(value) < 13}
print(stocks_A)

# %%
{key: 'Corp' if 'Corp' in value else 'Inc' for (key, value) in stocks.items()}

# %%
numbers = range(20)
numbers_dict = {}

for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2
print(numbers_dict)

# %%
num_dict = {key: key ** 2 for key in numbers if key % 2 == 0}

# %%
nested_dict =   {'001': {'price': 100},
                 '002': {'price': 40},
                 '003': {'price': 60}}

for key, value in nested_dict.items():
    print(key, value)

# %%
nested_dict =   {'001': {'price': 100, 'items': 4},
                 '002': {'price': 40, 'items': 9},
                 '003': {'price': 60, 'items': 8}}
# %%
{key:value['price'] for (key, value) in nested_dict.items()}

# %%
{key:value['price']* for (key, value) in nested_dict.items() if }












































































