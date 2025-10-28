# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:41:52 2024

@author: pogro
"""

import os
# %%
dir(os)

# %%
os.getcwd('..')

# %%
os.chdir('..')

# %%
os.system('mkdir dir1')

# %%
os.rmdir('dir1')

# %%
os.listdir()

# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)

# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
    
# %%
os.path.join(r'\home\user\bin', 'python') 


































