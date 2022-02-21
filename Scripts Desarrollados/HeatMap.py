# Script for graph heatmap

# Import librarys
import pandas as pd # Panda library for read and handle .csv file
import seaborn as sns # Library used to generate heatmap
import matplotlib.pyplot as plt # Matplotlib library used for make graphics

# Read the dataframe from .csv file previusly generated
df = pd.read_csv (r'Matriz_HealthAutomatico.csv')
# Set the index of the dataframe
df = df.set_index('Entidad')

# Iterate the dataframe
for i in df.index:
	# declare variable where the number of occurrences are saved
	count = 0
	# iterate through every colum of the row
	for j in df.index:
		# if the percentage of similarity is more or equal than 30
		if (df[j][i]) >= 30:
			# increase in 1 the count
			count = count + 1
	# if the coun ts less than two delete the entry
	if count < 2:
		df = df.drop(i, 0)
		df = df.drop(i, 1)

# get the names of every entity
lista = list(df.columns)

# generate the heatmap with the names of entitys en two axes
ax = sns.heatmap(df, xticklabels=lista, yticklabels=lista, annot=False, cmap="YlGnBu")


# Config fontsize
plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=13)    # fontsize of the tick labels
plt.rc('ytick', labelsize=13)    # fontsize of the tick labels

# configure the labels
plt.xlabel('entidad')
plt.ylabel('entidad')
# plot the graph
plt.show()


# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation




