# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:19:13 2024

@author: pogro
"""

techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file = file)
# %%
parzyste = list(range(100))[::2]

with open('numbers.txt', 'w') as file:
    for number in parzyste:
        file.write(str(number)+ '\n')
        
# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file: # append - dodawanie do pliku
    for tech in techs:
        print(tech, file = file)

# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)

# %%
with open('tree_2.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end = '', file = file)
            print('{}'.format('*' * i), file = file)

# %%
first_name = 'Jan'
last_name = 'Kowalski'
weight = 75.5
height = 1.85
date_of_birth = '1990-01-01'
chronic_conditions = ['hypertension', 'diabetes']
medications = {
    'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
    'diabetes_medications': ['metformin'],
}

with open('patient_data.txt', 'w') as file:
    file.write('First name: {}\n'.format(first_name))
    file.write('Last name: {}\n'.format(last_name))
    file.write('Weight: {}\n'.format(weight))
    file.write('Height: {}\n'.format(height))
    file.write('Date of birth: {}\n'.format(date_of_birth))
    file.write('Chronic conditions: {}\n'.format(', '.join(chronic_conditions)))
    file.write('Hypertension medications: {}\n'.format(', '.join(medications['hypertension_medications'])))
    file.write('Diabetes medications: {}\n'.format(', '.join(medications['diabetes_medications'])))
# %%


































