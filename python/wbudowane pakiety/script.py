# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:48:01 2024

@author: pogro
"""

import sys
 
# Open a file for writing
with open('output.txt', 'w') as file:
    # Use sys.stdout to redirect the standard output to a file
    sys.stdout = file
 
    # Print some output
    print('This output will be written to a file')
 
# The standard output is now back to the console
print('This output will be printed to the console')