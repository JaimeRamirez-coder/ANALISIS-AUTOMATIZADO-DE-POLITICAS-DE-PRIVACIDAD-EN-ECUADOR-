# Script for web scraping, find privacy policy url from main page of any entity


# Import librarys and other scripts
from selenium import webdriver # Library for web scraping
from selenium.webdriver.firefox.options import Options # Load options from gecko web driver
import time # Library used for control execution time

options = Options() # Asign options of webdriver to options
options.headless = True # Don't open gui of webdriver

# Configure webdriver with options and the path of gecko
# Webdriver used: Firefox
driver = webdriver.Firefox(options=options, executable_path='/home/ubuntu/Desktop/geckodriver')

# List of words that webdriver have to find
words = ["priv", "Priv", "legal", "aviso", "pol", "Pol"]

# Try to find any of the words
for i in words:
	try:
		# Give the main url of the entity
		driver.get("https://www.inclusion.gob.ec")
		
		# find if any floating message appears when window opens
		if len(driver.find_elements_by_xpath("//*[contains(text(), 'close')]")) != 0:
			# Asign the elements that where found to coincidence		
			coincidence = (driver.find_elements_by_xpath("//*[contains(text(), 'close')]"))
			# Iterate every close button
			for i in range(0,len(coincidence)):
				# if the button is showed
				if coincidence[i].is_displayed():
					# click on the button to close the message
					coincidence[i].click()
					
		# if there is not floating messages do nothing
		else:
			pass
		
		# find the link of policy url and open it
		pol_link = driver.find_element_by_partial_link_text(i).click()
		
		# Wait 2.4 seconds for bypass botdetection
		time.sleep(2.4)
		
		# Find if the url opens in new window
		if len(driver.window_handles) != 1:
			window_after = driver.window_handles[1]
			# if the url opens in new window switch webdriver to this window
			driver.switch_to.window(window_after)
			
			# Print the url of privacy url
			print(driver.current_url)
		
		# Print the url on the unique window open
		else:
			# Print the url of privacy url
			print(driver.current_url)
			
	except Exception as inst:
		# Control message
		print("no se pudo: "+i)
		
driver.quit() # Close webdriver

# Copyright © 2021, 2022 Jaime Patricio Ramírez Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation




