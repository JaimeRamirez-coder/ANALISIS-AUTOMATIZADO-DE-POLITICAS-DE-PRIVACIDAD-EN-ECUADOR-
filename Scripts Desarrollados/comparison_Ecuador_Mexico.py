# Script used to made comparison between Ecuador and Mexico

import nltk # Library used for count the number of words in policys
from os import listdir # Library used for iterate through
import pandas as pd # Panda library for read and handle .csv file

# find data in mexican policys and ecuadorian policys
folder2 = nltk.data.find("/home/ubuntu/Desktop/LimpiezaMexico")
folder1 = nltk.data.find("/home/ubuntu/Desktop/Limpieza")

# Empy arrays used for save data
eje_y_senten1 = []
eje_y_words1 = []
eje_y_senten2 = []
eje_y_words2 = []


# Iterate through every policy
for politica in sorted(listdir('/home/ubuntu/Desktop/Limpieza')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder1, politica)
	# Count the number of sentences on the policy and append to the array
	eje_y_senten1.append(len(corpusReader.sents()))
	# Count the number of words on the policy and append to the array
	eje_y_words1.append(len([word for sentence in corpusReader.sents() for word in sentence]))

# Iterate through every policy
for politica in sorted(listdir('/home/ubuntu/Desktop/LimpiezaMexico')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder2, politica)
	# Count the number of sentences on the policy and append to the array
	eje_y_senten2.append(len(corpusReader.sents()))
	# Count the number of words on the policy and append to the array
	eje_y_words2.append(len([word for sentence in corpusReader.sents() for word in sentence]))

# Variables used for calculete the average of words and sentenses
x = 0
sumx = 0
sum1x =0
y = 0
sumy = 0
sum1y =0

# Iterate through the amount of policys
for i in range(len(eje_y_senten1)):
	# sum all the numbers of words for every policy
	sumx = sumx + eje_y_senten1[i]
	# sum all the numbers of sentences for every policy
	sum1x = sum1x + eje_y_words1[i]
	# increase in one the number of policys
	x = x +1 
	
# calculete the average of words and sentenses for ecuadorean policys
promSenEC = sumx/x
promWordEC = sum1x/x

# Iterate through the amount of policys
for i in range(len(eje_y_senten2)):
	# sum all the numbers of words for every policy
	sumy = sumy + eje_y_senten2[i]
	# sum all the numbers of sentences for every policy
	sum1y = sum1y + eje_y_words2[i]
	# increase in one the number of policys
	y = y +1 

# calculete the average of words and sentenses for ecuadorean policys
promSenMX = sumy/y
promWordMX = sum1y/y

# generate arrays with the data needed
Palabras = [promWordEC, promWordMX]
Oraciones = [promSenEC, promSenMX]


# Print info on screen
print('Promedio de palabras por política')
print("Ecuador   México")
print(Palabras)

print('Promedio de Oraciones por política')
print("Ecuador   México")
print(Oraciones)


# Read the dataframe from .csv file previusly generated
df1 = pd.read_csv (r'Matriz_AutomatizadaMexico.csv')
# Set the index of the dataframe
df1 = df1.set_index('Entidad')

# Read the dataframe from .csv file previusly generated
df2 = pd.read_csv (r'Matriz_Automatizada.csv')
# Set the index of the dataframe
df2 = df2.set_index('Entidad')

# Iterate through the dataframe
for i in df1.index:
	# declare variable where the number of occurrences are saved
	count = 0
	# iterate through every colum of the row
	for j in df1.index:
		# if the percentage of similarity is more or equal than 30
		if (df1[j][i]) >= 80:
			# increase in 1 the count
			count = count + 1
	# if the coun ts less than two delete the entry
	if count < 2:
		df1 = df1.drop(i, 0)
		df1 = df1.drop(i, 1)

# Iterate through the dataframe
for i in df2.index:
	# declare variable where the number of occurrences are saved
	count = 0
	# iterate through every colum of the row
	for j in df2.index:
		# if the percentage of similarity is more or equal than 30
		if (df2[j][i]) >= 80:
			# increase in 1 the count
			count = count + 1
	# if the coun ts less than two delete the entry
	if count < 2:
		df2 = df2.drop(i, 0)
		df2 = df2.drop(i, 1)


# Print on screen dataframes from Ecuador and Mexico
print(df2)
print(df1)

# Print amount of policys with more than 80% of similarity 
printl('Políticas con más del 80% de similitud')
print("Ecuador  México")
print(len(df2), len(df1))




# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation





