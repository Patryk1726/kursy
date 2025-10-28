# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:17:02 2024

@author: pogro
"""

class Drzewo:
    
    def wyswietl_info_o_drzewie(self):
        self.nazwa = 'Sosna'
        self.wiek = 30
        print(f'Drzewo {self.nazwa} ma {self.wiek} lat.')
    
drzewo = Drzewo()
# %%

drzewo.wyswietl_info_o_drzewie() # to samo

# %%
Drzewo.wyswietl_info_o_drzewie(drzewo) # to samo