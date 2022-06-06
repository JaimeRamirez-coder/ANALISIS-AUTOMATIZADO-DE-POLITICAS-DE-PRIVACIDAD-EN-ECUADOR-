# Script used for calculate similarity and generate .csv file with similarity values

# Import librarys
from os import listdir # Library used for iterate through
import pandas as pd # Panda library for read and handle .csv file
import numpy as np # Library used for complex math operations
from nltk.corpus import stopwords # nltk tool used to get dictionary of stopwords
from nltk.tokenize import word_tokenize # nltk tool used to generate tokens form words

# Empy arrays used for save data
definitiva = []
ejes = []

# add colum name to the array
definitiva.append("Entidad")

# Iterate through every policy
for politica in listdir('/home/ubuntu/Desktop/LimpiezaMexico'):
	# Add entity names to the array
	definitiva.append(politica.removesuffix('.txt'))

# Iterate through every policy
for politica in listdir('/home/ubuntu/Desktop/LimpiezaMexico'):
	# generate the path for the policy
	pol = "/home/ubuntu/Desktop/LimpiezaMexico/"+str(politica)
	# Open the policy in read mode
	g = open(pol, "r")
	# read the text of the policy
	X = g.read()
	#print(politica,"======================================================")
	
	# Empy arrays where percetage of similarity will be save
	lista = []
	
	# add entity name in two arrays
	ejes.append(politica.removesuffix('.txt'))
	lista.append(politica.removesuffix('.txt'))
	
	# Iterate through every policy
	for politica in listdir('/home/ubuntu/Desktop/LimpiezaMexico'):
		# generate the path for the policy
		pol = "/home/ubuntu/Desktop/LimpiezaMexico/"+str(politica)
		# Open the policy in read mode
		g = open(pol, "r")
		# read the text of the policy
		Y = g.read()
		
		# generate tokens from the policys that are been compared
		X_list = word_tokenize(X.lower()) 
		Y_list = word_tokenize(Y.lower())
		 
		# Auxiliar arrays
		l1 =[]
		l2 =[]
		
		# generate an array with spanish stop words
		sw = set(stopwords.words('spanish'))
		
		# Delete stopwords from the privacy policys
		X_set = {w for w in X_list if not w in sw}  
		Y_set = {w for w in Y_list if not w in sw}
		
		# Generate and array with words tokenized form the policys
		total_array = X_set.union(Y_set)
		
		# iterate through every token in the array
		for w in total_array:
			# evaluate the array in order to detect in what policy it is contained
			
			# if the wor is in the first policy
			if w in X_set:
				# add a "1" to the array
				l1.append(1)
			# else add a "0"
			else: l1.append(0)
			# if the wor is in the first policy
			if w in Y_set:
				# add a "1" to the array
				l2.append(1)
			# else add a "0"
			else: l2.append(0)
		
		# auxiliar variable use to calculate the sum
		c=0
		
		#### Cosine similarity formula ###
		
		# Calculate the sum of the product of the arrays
		for i in range(len(total_array)):
			c+= l1[i]*l2[i]
		
		# Calculate the cocine similarity
		cosine = c / float((sum(l1)*sum(l2))**0.5)
		
		# get the percentage of similarity
		similaridad = cosine*100
		
		# add simiarity percentage to the array
		lista.append(similaridad)
		#print(politica,"==============")
		#print("similaridad: ", round(similaridad,2), "%", sep="")
	
	# after all the similaritys are calculated for one entity stack it array to the  array
	definitiva = np.vstack([definitiva, lista])

# generate the dataframe
df = pd.DataFrame(definitiva)
# made the first colum as the name of entrys
df.rename(columns=df.iloc[0], inplace = True)
# errase the first empy entry
df.drop(df.index[0], inplace = True)

# Set the index of the dataframe
df = df.set_index('Entidad')

# Save dataframe as .csv file
df.to_csv('Matriz_AutomatizadaMexico.csv')

# print dataframe on screen
print(df)




# Copyright © 2021, 2022 Jaime Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
