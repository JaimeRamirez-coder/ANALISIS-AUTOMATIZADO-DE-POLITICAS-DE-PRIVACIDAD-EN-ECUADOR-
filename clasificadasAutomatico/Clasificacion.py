import pandas as pd
from pathlib import Path
from os import listdir
import os


df = pd.read_csv("/home/ubuntu/Desktop/lista_sitios_ecuador_jaej_modificada.csv")


categorias = []


for politica in listdir('/home/ubuntu/Desktop/Limpieza'):
	politica = politica.removesuffix('.txt')
	categoria = df.loc[df['Entity URL'] == politica, 'Category'].iloc[0]
	categorias.append(categoria)

myset = set(categorias)
print(myset)

for dirName in myset:
	if not os.path.exists(dirName):
    		os.makedirs(dirName)





for politica in listdir('/home/ubuntu/Desktop/Limpieza'):
	
	pol = "/home/ubuntu/Desktop/politicas/"+str(politica)
	g = open(pol, "r")
	X = g.read()
	
	politica = politica.removesuffix('.txt')
	
	categoria = df.loc[df['Entity URL'] == politica, 'Category'].iloc[0]
	
	politi = "/home/ubuntu/Desktop/clasificadasAutomatico/"+categoria+"/"+politica+".txt"
	Path(politi).touch()
	with open(politi, 'a') as f:
		f.write(X)
			
			
			
			







	
