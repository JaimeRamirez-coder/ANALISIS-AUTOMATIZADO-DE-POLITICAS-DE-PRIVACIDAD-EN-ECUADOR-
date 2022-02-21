# Script for clean noise in policys

# Import librarys 
from os import listdir # Library used for iterate through
from pathlib import Path # Used for get path of files
import matplotlib.pyplot as plt # Matplotlib library used for make graphics
import numpy as np # Library used for complex math operations

# Empy arrays used for save data to be ploted
eje_x = []
eje_y = []

# Variables declaration
total = 0
limpias = 0
listapos = 0
listaneg = 0
sucias = 0

# Create a .txt file for save the name of entitys that cant be cleaned
Path("/home/ubuntu/Desktop/RuidosasMexico.txt").touch()

# Iterate through every policy
for politica in listdir('/home/ubuntu/Desktop/politicas'):
	# generate the path for specific policy
	pol = "/home/ubuntu/Desktop/politicas/"+str(politica)
	# open the file of the policy
	g = open(pol, "r")
	# read the policy
	Y = g.read()
	# transform every letter to lower case
	y = Y.lower()
	# variables used to control the filter aplication in order to get the firts occurrence
	index0 = 0
	index = 99999
	
	# Iterate through every word in the filter database
	for a in ['tica de privacidad', 'ticas de privacidad', 'rminos y condiciones', 'aviso legal', 'política para el tratamiento de datos', 'ticas de uso', 'declaración de privacidad', 'código de ética', 'información legal', 'aviso de privacidad', 'rminos de Uso', 'tica global de privacidad', 'tica de protección de datos', 'tica de uso', 'avisos de privacidad', 'Aviso integral de privacidad']:
		# find the index where the filter find an occurrence
		index0 = y.find(a)
		# if there is an occurrence
		if index0 != -1:
			# if the word is before the previus found
			if index0 < index:
				# set the new value of the index
				index = index0	
	# increse in one "total" variable
	total = total +1
	
	# if an ocurrence was found
	if index != 99999:
		
		# increse in 1 the amount of clean policys
		limpias = limpias +1
		# extract the text of the policy after the index
		polFin = y[index:]
		# generate an array with every word of the policy
		word_list = y.split()
		# get the length of the array
		A = len(word_list)
		
		# generate an array with every word of the clean policy
		word_list = polFin.split()
		# get the length of the array
		B = len(word_list)
		
		# Get the percentage of words that have been deleted 
		percentage = (1-B/A)*100

		# if the percentage is less tha 25%
		if percentage < 25:
			# increase in 1 the amount of policys with less than 25% cleaned
			listaneg = listaneg + 1
		else:
			# increase in 1 the amount of policys with more than 25% cleaned
			listapos = listapos + 1
		# generate the path for the new policy
		politi = "/home/ubuntu/Desktop/Limpiez/"+politica
		# Create the empy file
		Path(politi).touch()
		# writhe the clean policy in the new file
		with open(politi, 'a') as f:
			f.write(polFin)
		
		# add the policy name and the percentage of words cleaned to arrays
		eje_x.append(politica.removesuffix('.txt'))
		eje_y.append(percentage)

	# if there is no ocurrences	
	else:
		# increse the amount of "noise policys"
		sucias = sucias + 1
		
		# set the index in 0 
		index = 0
		
		# increse in 1 the amount of clean policys in order to get control of proccesed policys
		limpias = limpias +1
		
		# extract the text of the policy after the index
		polFin = y[index:]
		# generate an array with every word of the policy
		word_list = y.split()
		# get the length of the array
		A = len(word_list)

		# generate an array with every word of the clean policy
		word_list = polFin.split()
		# get the length of the array
		B = len(word_list)

		# Get the percentage of words that have been deleted 
		percentage = (1-B/A)*100

		# if the percentage is less tha 25%
		if percentage < 25:
			# increase in 1 the amount of policys with less than 25% cleaned
			listaneg = listaneg + 1
		else:
			# increase in 1 the amount of policys with more than 25% cleaned
			listapos = listapos + 1
		# generate the path for the new policy
		politi = "/home/ubuntu/Desktop/Limpiez/"+politica
		# Create the empy file
		Path(politi).touch()
		# writhe the clean policy in the new file
		with open(politi, 'a') as f:
			f.write(polFin)
		
		# add the policy name and the percentage of words cleaned to arrays
		eje_x.append(politica.removesuffix('.txt'))
		eje_y.append(percentage)
		
		# append the name of policy to the file to get control of policys where the filter fails
		with open("/home/ubuntu/Desktop/RuidosasMexico.txt", 'a') as f:
			f.write(politica+"\n")

# create copy of arrays where the data is saved
list1 = eje_y
list2 = eje_x

# generate tuples with data in to arrays
zipped_lists = zip(list1, list2)
# sort the tuples
sorted_pairs = sorted(zipped_lists)

# unzip the tuples in two arrays
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

# Config fontsize
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=12)    # fontsize of the x and y labels

# plot bar chart
plt.figure(1)
plt.barh(list2, list1)
# labels of the bar chart
plt.ylabel('entidad')
plt.xlabel('porcentaje de contenido no relacionado con la política de privacidad')
# config the limits of the graph
plt.xlim(0, 100)
plt.ylim(-1, len(list2))
# generate an array with percentages
ind = np.arange(0,100,10)
# generate a complex graph
ax = plt.gca()
# set the labes of X
ax.set_xticks(ind)
# config and enable grid
ax.grid(which='major', axis='y', linestyle='--')
plt.grid()
# plot the graph
plt.show()


# Config fontsize
plt.rc('font', size=20)          # controls default text sizes
plt.rc('legend', fontsize=18)    # legend fontsize

# Plot percentage 
cantidad2 = [listaneg,listapos]
# legends of the chart
nombres2 = ["Politicas en las que \nse limpio menos del 25%","Politicas en las que \nse limpio más del 25%"]
plt.figure(2)
plt.pie(cantidad2, autopct="%0.1f %%")
# configure the position of the legend
plt.legend(nombres2, bbox_to_anchor=(0.85,1.025), loc="upper left")
plt.show()


# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

	
