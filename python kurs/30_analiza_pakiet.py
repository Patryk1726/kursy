# -*- coding: utf-8 -*-
import sys
sys.path.append(r'C:\Users\pogro\repozytoria\python kurs\moduły')
import rocket.data

# %%
dir(rocket.data)

# %%
dane = rocket.data.get_data()

# %%
import rocket.algorytmy

# %%
rocket.algorytmy.drzewa_decyzyjne()

# %%
from rocket.algorytmy import drzewa_decyzyjne

# %%
drzewa_decyzyjne()
# %%
from rocket.funkcje.stats import mean

# %%
mean(dane)