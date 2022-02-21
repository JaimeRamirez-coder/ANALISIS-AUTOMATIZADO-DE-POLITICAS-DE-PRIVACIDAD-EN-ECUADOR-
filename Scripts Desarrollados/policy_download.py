# Script for download and save policys with entity name and date of recolection


# Import librarys and other scripts
import pandas as pd # Panda library for read and handle .csv file
from pathlib import Path # Library for create .txt file for every policy
from policy_extract import policy_extract # Import script that download .html or .pdf file with the policy
from datetime import date # Library that get the date

# Read and define de Data Frame from de .csv file
df = pd.read_csv("/home/ubuntu/Desktop/lista_sitios_mexico_jaej_modificada.csv")

# save in url the colum Policy URL and Entity URL 
url = df.loc[:,["Policy URL","Entity URL"]]

# Varible for iterate the entity URL in the url Data Frame
i=0

# Create string with the date of the recolection
date = ("date de recoleccion: " + str(date.today()) + "\n")

# Iterate every raw in url Data Frame
for url1 in url.loc[:,"Policy URL"]:
  # Print every url on console to control the procces
  print(url1)
  
  # Some policys cant be extracted and creat exceptions
  try:
    # Extract text form .html or .pdf file with the script created
    text = policy_extract(url1)
    # Create string with the path of the policy
    Policy_path = "/home/ubuntu/Desktop/politicasMexico/"+url.loc[i,"Entity URL"]+".txt"
    # Create the .txt file
    Path(Policy_path).touch()
    # Create .txt with the Entity URL and open it with append privilege
    with open(Policy_path, 'a') as file:
      # add the date of recolection at the beginning of the policy
      file.write(date)
      # write the text extracted from the html or pdf file to the .txt file
      file.write(text)
      # Close the policy
      file.close
    # Prin on console the policy path 
    print(Policy_path)
    # Increase i for iterate on url Data Frame
    i=i+1
  except Exception as inst:
    # Print error mesagge on console for USER
    print("===========================>>> ERROR ")
    
    # Increase i for iterate on url Data Frame
    i=i+1
    
    
# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation


