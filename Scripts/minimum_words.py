# Script that calculate and graph the amount of policys with more than 3000 words

# Import librarys
import nltk # Library used for NLP
from os import listdir # Library used for iterate through
import matplotlib.pyplot as plt # Matplotlib library used for make graphics


plt.rc('font', size=18)          # controls default text sizes
plt.rc('legend', fontsize=18)    # legend fontsize


# Generate an object that have indexed all files in the 
folder2 = nltk.data.find("/home/ubuntu/Desktop/Limpieza") 

# Empty array to store the amount of words in every policy
words2 = []

# Iterate through every policy
for politica in sorted(listdir('/home/ubuntu/Desktop/Limpieza')):
	# Generate a corpus for every policy in the folder
	corpusReader = nltk.corpus.PlaintextCorpusReader(folder2, politica)
	# Count the number of words on the policy and append to the array
	words2.append(len([word for sentence in corpusReader.sents() for word in sentence]))
	
# count the number of policys
total = len(words2)

# Variable to count policys with less than 3000 words
mayoria = 0

# iterate through every number of words
for i in words2:
	# if the number of words is less or equal than 3000
	if i <= 3000:
		# increase in one the counter
		mayoria = mayoria + 1

# Calculate the percentage of policys with less or equal than 3000 words
porcentaje = mayoria / total * 100

# Calculate the percentage of policys with more than 3000 words
resto = 100 - porcentaje

# Graph pie chart
cantidad2 = [porcentaje,resto]
# legends of the chart
nombres2 = ["politicas con menos de 3000 palabras","politicas con más de 3000 palabras"]
plt.pie(cantidad2, autopct="%0.1f %%", startangle=90)
# configure the position of the legend
plt.legend(nombres2, bbox_to_anchor=(0.85,1.025), loc="upper left")
plt.show()










