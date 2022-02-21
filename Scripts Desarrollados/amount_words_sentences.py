# Script that calculete the amount of words and sentences on privacy policys

# Import librarys
import nltk # Library used for count the number of words in policys
from os import listdir # Library used for iterate through
import matplotlib.pyplot as plt # Matplotlib library used for make graphics
import numpy as np # Library used for complex math operations

# find data in policys, clean policys with filter and manually clean policys 
folder2 = nltk.data.find("/home/ubuntu/Desktop/LimpiezaMexico")
folder1 = nltk.data.find("/home/ubuntu/Desktop/LimpiezaManualMexico")
folder = nltk.data.find("/home/ubuntu/Desktop/politicasMexico")

# Config fontsize
plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels


# Empy arrays used for save data
eje_x_2 = []
eje_x_3 = []
eje_y_senten = []
eje_y_words = []
eje_y_senten1 = []
eje_y_words1 = []
eje_y_senten2 = []
eje_y_words2 = []



# Iterate through every policy
for politica in sorted(listdir('/home/ubuntu/Desktop/politicasMexico')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder, politica)
	# Count the number of sentences on the policy and append to the array
	eje_y_senten.append(len(corpusReader.sents()))
	# Count the number of words on the policy and append to the array
	eje_y_words.append(len([word for sentence in corpusReader.sents() for word in sentence]))
	# get the entity names
	eje_x_2.append(politica.removesuffix('.txt'))
	eje_x_3.append(politica.removesuffix('.txt'))

# Iterate through every clean policy
for politica in sorted(listdir('/home/ubuntu/Desktop/LimpiezaManualMexico')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder1, politica)
	# Count the number of sentences on the policy and append to the array
	eje_y_senten1.append(len(corpusReader.sents()))
	# Count the number of words on the policy and append to the array
	eje_y_words1.append(len([word for sentence in corpusReader.sents() for word in sentence]))

# Iterate through every manually clean policy
for politica in sorted(listdir('/home/ubuntu/Desktop/LimpiezaMexico')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder2, politica)
	# Count the number of sentences on the policy and append to the array
	eje_y_senten2.append(len(corpusReader.sents()))
	# Count the number of words on the policy and append to the array
	eje_y_words2.append(len([word for sentence in corpusReader.sents() for word in sentence]))

	

# Copy arrays
list1 = eje_y_senten
list2 = eje_x_2
list3 = eje_y_senten1
list4 = eje_y_senten2
# generate a triple
zipped_lists = zip(list1, list2, list3, list4)
# sort elements 
sorted_pairs = sorted(zipped_lists)
# create 3 arrays 
tuples = zip(*sorted_pairs)
list1, list2, list3, list4 = [ list(tuple) for tuple in  tuples]

# Generate an index of the position of every entity
ind = np.arange(len(list2))
# width of separation between
width = 0.25

# generate subplots
fig, ax = plt.subplots()

# roteta names on x axis
plt.xticks(rotation=90)
#  plot bar graph
plt.bar(ind - width, list3, width, label="Políticas limpias (limpieza manual)")
plt.bar(ind, list4, width, label="Políticas limpias (limpieza automatizada)")
plt.bar(ind + width, list1, width, label="Políticas sin limpiar")
# set labels
plt.ylabel('cantidad de oraciones por politica')
plt.xlabel('entidad')
# set names on x axes
ax.set_xticks(ind)
ax.set_xticklabels(list2)
# config and enable grid
ax.grid(which='major', axis='x', linestyle='--', linewidth='0.25')
plt.grid()
# config limits of the graph
plt.xlim(-0.5, len(list2)-0.5)
# plot the graph
plt.legend()
plt.show()



# Copy arrays
list1 = eje_y_words
list2 = eje_x_3
list3 = eje_y_words1
list4 = eje_y_words2
# generate a triple
zipped_lists = zip(list1, list2, list3, list4)
# sort elements 
sorted_pairs = sorted(zipped_lists)
# create 3 arrays 
tuples = zip(*sorted_pairs)
list1, list2, list3, list4 = [ list(tuple) for tuple in  tuples]

# Generate an index of the position of every entity
ind = np.arange(len(list2))
# width of separation between
width = 0.25
# generate subplots
fig, ax = plt.subplots()

# roteta names on x axis
plt.xticks(rotation=90)
#  plot bar graph
plt.bar(ind - width, list3, width, label="Políticas limpias (limpieza manual)")
plt.bar(ind, list4, width, label="Políticas limpias (limpieza automatizada)")
plt.bar(ind + width, list1, width, label="Políticas sin limpiar")
# set labels
plt.ylabel('cantidad de palabras por política')
plt.xlabel('entidad')
# set names on x axes
ax.set_xticks(ind)
ax.set_xticklabels(list2)
# config and enable grid
ax.grid(which='major', axis='x', linestyle='--')
plt.grid()
# config limits of the graph
plt.xlim(-0.5, len(list2)-0.5)
# plot the graph
plt.legend()
plt.show()



# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation


