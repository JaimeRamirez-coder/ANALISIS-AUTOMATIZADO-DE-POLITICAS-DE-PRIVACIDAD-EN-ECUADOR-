# Script for generate word cloud


# Import librarys

# Basic librarys
import numpy as np # Library used for complex math operations
import pandas as pd  # Panda library for read and handle .csv file
from os import listdir # Library used for iterate through policys

# word cloud librarys
from PIL import Image # used for image edition
from wordcloud import WordCloud, ImageColorGenerator # Library that generates word cloud

#  Text proccesing librarys
import string # List of pre-initialized strings
import nltk # Library used for NLP
from nltk.corpus import stopwords # List of stop words

# empy vector used for save sets of punctuation_set
punctuation_set=[]
# iterate through the pre-initialized string with punctuations
for s in string.punctuation_set:
	# add every punctuation_set to the vector
	punctuation_set.append(str(s))

# generate another vector with more punctuation_set
punctuation_extra = ["¿", "¡", "“", "”", "…", ":", "–", "»", "«"]    

# Concatenate the two vectors with punctuation_set
punctuation_set += punctuation_extra

# get the list of stop words in spanish
stop_words = stopwords.words('spanish')

# Empy string where all text from policys will be saved
texto = ""

# iterate through policys
for politica in listdir('/home/ubuntu/Desktop/LimpiezaManualMexico'):
	#if politica != "epn.edu.ec.txt" and politica != "mercadolibre.com.ec.txt" and politica != "bgr.com.ec.txt":
	# dont process mercado libre policy because it has too many noise
	if politica != "mercadolibre.mx.txt":
		# generate the path for the policy
		pol = "/home/ubuntu/Desktop/LimpiezaManualMexico/"+str(politica)
		# Open the policy in read mode
		g = open(pol, "r")
		# read the text of the policy
		Y = g.read()
		# add text of the policy to the string
		texto += Y

# Declare a string where clean text will be saved
clean_texto = ""

# iterate through every punctuation on the vector
for p in punctuation_set:
	# delete every punctuation after made it lower case
	clean_texto = texto.lower().replace(p,"")
# iterate through every punctuation on the vector
for p in punctuation_set:
	# delete every punctuation 
	clean_texto = clean_texto.replace(p,"")

# iterate through every stop word
for stop in stop_words:
	# generate a vector with every word in the clean string
	clean_texto_list = clean_texto.split()
	# delete blank spaces at the begining and end of the string
	clean_texto_list = [i.strip() for i in clean_texto_list]
	try:
		# remove every occurrence of the stop word in the string
		while stop in clean_texto_list: clean_texto_list.remove(stop)
	except:
		# not concider in case of error
		pass
	# add a blank space between text
	clean_texto= " ".join(clean_texto_list)

# generate a vector with strings
text_vector = clean_texto.split(" ")

# empy vector
normal_words = []

# Iterate every word in text vector
for palabra in text_vector:
	# only concider words with length more than 3 and less than 18
	if (len(palabra)>=3 and len(palabra)<18):
		normal_words.append(palabra)

# generate a hash table in order to handle frecuency of words
word_count={}

# Iterate every word in the normal word list
for palabra in normal_words:
	# if the key already exist in the hash table
	if palabra in word_count.keys():
		# increace in 1 the counter
		word_count[palabra][0]+=1
	# create the entry inthe hash table and add 1 to teh counter
	else:
		word_count[palabra]=[1]

word_count

# Generate a dataframe from the hash table
df = pd.DataFrame.from_dict(word_count).transpose()
# add title to the colum
df.columns=["freq"]
# sort values on the dataframe
df.sort_values(["freq"], ascending=False, inplace=True)
# print top 10 entries in the dataframe
df.head(10)


# open the picture used for the word cloud in this case is a cloud
picture = Image.open("./nube.png").convert("RGBA")
# Create a new picture with white color 
image = Image.new("RGB", picture.size, "WHITE")
# paste the picture loaded on the blank picture generated 
image.paste(picture, (0, 0), picture)
# Create an array with the picture
mask = np.array(image)

# generate a word cloud 
word_cloud = WordCloud(mask=mask, background_color='white', contour_width=1, contour_color='grey', max_words=200, min_font_size=5, collocation_threshold=10).generate(clean_texto)

# Save word cloud picture
word_cloud.to_file("./nube_privacidad3.png")


# Copyright © 2021, 2022 Jaime Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation



