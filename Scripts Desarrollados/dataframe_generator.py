# Script for generate dataframe of privacy policys

# Import librarys
import pandas as pd # Panda library for read and handle .csv file
import numpy as np # Library used for complex math operations
from os import listdir # Library used for iterate through policys

# Create empy arrays to save data
definitiva = []
Entidad = []

# Varible for iterate in Data Frame
i = 0

# Generate titles for every colum of the dataframe
definitiva.append("Entidad")
definitiva.append("text")

# Iterate through every policy
for politica in listdir('/home/ubuntu/Desktop/LimpiezaManual/'):
	# add the entity name to the entity array
	Entidad.append(politica.removesuffix('.txt'))

# Iterate through every policy
for politica in listdir('/home/ubuntu/Desktop/LimpiezaManual'):
	# Empy variable where the text of policy is saved
	data = ''
	# Read the text of the policy
	with open("/home/ubuntu/Desktop/LimpiezaManual/"+str(politica), 'r') as file:
		data = file.read()
	
	# generate empy array
	lista = []
	
	# add the entity name to the array 
	lista.append(Entidad[i])
	# add the text of the policy to the array
	lista.append(data)
	
	# stack the new entry to the array 
	definitiva = np.vstack([definitiva, lista])
	
	# increase in 1 the value of i 
	i = i+1

# generate the dataframe
df = pd.DataFrame(definitiva)
# made the first colum as the name of entrys
df.rename(columns=df.iloc[0], inplace = True)
# errase the first empy entry
df.drop(df.index[0], inplace = True)

# Save dataframe as .csv file
df.to_csv('Policys.csv')

# Print dataframe
print(df)


# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation



