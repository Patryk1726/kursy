# -*- coding: utf-8 -*-

import sys
sys.path.append(r'C:\Users\pogro\repozytoria\python kurs\moduły')
import rocket_science

# %%
dir(rocket_science)

# %%
rocket_science.calculate_mean([3, 4])
rocket_science.calculate_min([3, 4])
rocket_science.calculate_max([3, 4])

# %%
from rocket_science import calculate_mean # najbardziej rekomendowany sposob

# %%
calculate_mean([2, 3])

# %%
from rocket_science import *

# %%
calculate_mean([4, 2])

# %%
from rocket_science import calculate_min, calculate_max
