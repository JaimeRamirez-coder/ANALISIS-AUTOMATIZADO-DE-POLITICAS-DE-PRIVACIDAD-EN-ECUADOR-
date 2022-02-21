# Script that calculete and graph the filter efficiency

# Import librarys
import nltk # Library used for count the number of words in policys
from os import listdir # Library used for iterate through
import matplotlib.pyplot as plt # Matplotlib library used for make graphics

# Declare the path of policys, clean policys with filter and manually clean policys 
folder2 = nltk.data.find("/home/ubuntu/Desktop/Limpieza")
folder1 = nltk.data.find("/home/ubuntu/Desktop/LimpiezaManual")
folder = nltk.data.find("/home/ubuntu/Desktop/politicas")

# Empy arrays used for save data
eje_x_2 = []
eje_y_words1 = []
eje_y_words2 = []



# Iterate through every policy
for politica in sorted(listdir('/home/ubuntu/Desktop/politicas')):
	# get the entity names
	eje_x_2.append(politica.removesuffix('.txt'))

# Iterate through every clean policy
for politica in sorted(listdir('/home/ubuntu/Desktop/LimpiezaManual')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder1, politica)
	# Count the number of words on the policy and append to the array
	eje_y_words1.append(len([word for sentence in corpusReader.sents() for word in sentence]))

# Iterate through every manually clean policy
for politica in sorted(listdir('/home/ubuntu/Desktop/Limpieza')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder2, politica)
	# Count the number of words on the policy and append to the array
	eje_y_words2.append(len([word for sentence in corpusReader.sents() for word in sentence]))

	
# Copy arrays
list2 = eje_x_2
list3 = eje_y_words1
list4 = eje_y_words2

# generate a triple
zipped_lists = zip(list2, list3, list4)
# sort elements 
sorted_pairs = sorted(zipped_lists)
# create 3 arrays 
tuples = zip(*sorted_pairs)
list2, list3, list4 = [ list(tuple) for tuple in  tuples]

# empy array where efficiency will be saved
eficiencia = []

# iterate every element in list
for i in range(len(list3)):
	# calculate efficiency
	efi = (list3[i]-6) / list4[i] * 100
	# add value of correct deviation to the array
	eficiencia.append(efi)


# Config fontsize
plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels

# generate subplots
fig, ax = plt.subplots()

#  plot bar graph
plt.xticks(rotation=90)
plt.bar(list2, eficiencia)
# set labels
plt.ylabel('Porcentaje de eficiencia')
plt.xlabel('Entidad')
#config and enable grid
ax.grid(which='major', axis='x', linestyle='--')
plt.grid()
# config limits of the graph
plt.xlim(-0.5, len(list2)-0.5)
# plot the graph
plt.show()



# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation



