# Script used for topic modelling

# Basic librarys
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from os import listdir
# Lybrary used for preproccessing
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
# Topic Modelling library
import gensim
from gensim.models import CoherenceModel, LdaModel
from gensim.models.wrappers import LdaMallet
from gensim.corpora import Dictionary
# Pretrained model for spanish
import spacy
nlp = spacy.load('es_core_news_md')
# library used for visualization of LDA models
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
# Library used in order to stop printing warnings on screen
import warnings
warnings.filterwarnings("ignore") 


# Read the dataframe from .csv file previusly generated
df = pd.read_csv (r'Policys.csv')
# errase the first empy entry
df.drop(df.index[0], inplace = True)
# Drop first column of dataframe
df = df.iloc[: , 1:]


# list of noise words that want to delete
black_list = ["rumi", "uso", "sitios"]

# function used to clean text
def cleaner(word):
	# function used in order to delete noise from the text the use of regular expresions is very useful
	word = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', '', word, flags=re.MULTILINE)
	word = re.sub(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', "", word)
	word = re.sub(r'\#\.', '', word)
	word = re.sub(r'\n', '', word)
	word = re.sub(r',', '', word)
	word = re.sub(r'\-', ' ', word)
	word = re.sub(r'\.{3}', ' ', word)
	word = re.sub(r'a{2,}', 'a', word)
	word = re.sub(r'é{2,}', 'é', word)
	word = re.sub(r'i{2,}', 'i', word)
	word = re.sub(r'ja{2,}', 'ja', word) 
	word = re.sub(r'á', 'a', word)
	word = re.sub(r'é', 'e', word)
	word = re.sub(r'í', 'i', word)
	word = re.sub(r'ó', 'o', word)
	word = re.sub(r'ú', 'u', word)  
	word = re.sub('[^a-zA-Z]', ' ', word)
	# empy array used to save clean words
	list_word_clean = []
	# iterate through every word
	for w1 in word.split(" "):
		# made lower case every word and add it to the clean word list if it isnot a stop word
		if  w1.lower() not in stopwords:
			list_word_clean.append(w1.lower())
	
	# generategenerate bigram from the clean words
	bigram_list = bigram[list_word_clean]
	# lematice every word
	out_text = lemmatization(" ".join(bigram_list))
	# return clean words lematiced
	return out_text

# Function used for lematization or get the root of the words
def lemmatization(texts, allowed_postags=['NOUN']):
	texts_out = [ token.text for token in nlp(texts) if token.pos_ in allowed_postags and token.text not in black_list and len(token.text)>2]
	# return text lematized
	return texts_out

# Get sentences in order to get more complex linguistic structures
bigram = gensim.models.Phrases(df.text.to_list()) 

# Get the list of stop words in spanish
stop = set(stopwords.words('spanish'))
# Generate the black list
additional_stopwords=set(black_list)
# Combine the black list and stopwords in one vector
stopwords = stop.union(additional_stopwords)

# apply cleaner function to the text of every policy
df['text'] = df['text'].apply(cleaner)

# generate a dictionary with the id and words
dictionary = Dictionary(df['text'].to_list())
# delete gaphs in the dictionary
dictionary.compactify()

# Filter extremes in the dictionary word that dont appear too much 
dictionary.filter_extremes(no_below=2, no_above=0.97, keep_n=None)
# delete gaphs in the dictionary
dictionary.compactify()

# generate touples with token id and frecuency of ocurrence
corpus = [dictionary.doc2bow(text) for text in df['text'].to_list()]

# Function that print topics on screen
def display_topics(model, model_type="lda"):
	# Iterate through topics
	for topic_idx, topic in enumerate(model.print_topics()):
		# print the number of topic
		print ("Tópico %d:" % (topic_idx))
		if model_type== "lda":
			# Print relevant words of the topic
			print (" ".join(re.findall( r'\"(.[^"]+).?', topic[1])), "\n")


# function used for generate a coherence vs number of topics graph
def coherence_graph(dictionary, corpus, texts, limit, model):
	# Empy arrays
	c_v = []
	lm_list = []
	# Iterate through the number of topics
	for num_topics in range(1, limit):
		# generate a model
		lm = LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary)
		# add model to the list
		lm_list.append(lm)
		# calculete coherence of the model
		cm = CoherenceModel(model=lm, texts=texts, dictionary=dictionary, coherence='c_v')
		# add coherence to the array
		c_v.append(cm.get_coherence())

	# Show graph
	x = range(1, limit)
	plt.xticks(x)
	plt.plot(x, c_v)
	plt.xlabel("Tópicos")
	plt.ylabel("Coherencia")
	plt.grid()
	plt.show()
	
	# return arrays with models and coherence
	return lm_list, c_v


# Generate a graph coherence vs number of topics 
lmlist_lda, c_v = coherence_graph(dictionary=dictionary, corpus=corpus, texts=df['text'].to_list(), limit=21, model= "lda")

# Ask the user what number of topics want
num = int(input("Ingrese la cantidad de topicos a evaluar: "))
# Get the number of topics selected by the user
ldamodel = lmlist_lda[num-1]

# print topics on screen
display_topics(ldamodel, model_type="lda")
# print coherence of the model on screen
print("Coherencia: ", c_v[num-1])


# generate a model visualization
model_display = gensimvis.prepare(ldamodel, corpus, dictionary, sort_topics=False)
# save interactive HTML file
pyLDAvis.save_html(model_display, 'ldaMexico.html')


# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

