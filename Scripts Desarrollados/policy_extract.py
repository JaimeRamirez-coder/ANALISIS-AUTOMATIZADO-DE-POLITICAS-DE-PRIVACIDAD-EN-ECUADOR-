# Script for download Privacy Policy Form .csv with links of policys

# Import libraries and other scripts
from io import StringIO # Library used for 

# Import modules from pdfminer, used for download policy that is pdf file and convert it to .txt file
from pdfminer.converter import TextConverter 
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# Import libraries for simple web scraping
import requests
import html2text


# Function that convert pdf file to .txt
def pdf_download(path):
	# Create i/o string
	policy = StringIO()
	# open the .PDF file
	with open(path, 'rb') as in_file:
		# Create pdf parser
		parser = PDFParser(in_file)
		# Create pdf document
		doc = PDFDocument(parser)
		# Create pdf handler
		rsrcmgr = PDFResourceManager()
		# Create pdf device that saves txt in policy
		device = TextConverter(rsrcmgr, policy, laparams=LAParams())
		# Create pdf interpreter that read text in every page of the pdf file
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		# Iterate every page of odf
		for page in PDFPage.create_pages(doc):
			# Get text of the page
			interpreter.process_page(page)
	# Return the text of pdf file
	return(policy.getvalue())

# Function that saves the content of privacy policy on .txt file
def policy_extract(url):
	# Create header for web craping, this bypass simple bot detectors
	# Emulate Mindows machine with mozilla firefox as web explorer
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
		"Accept-Encoding": "*",
		"Connection": "keep-alive"
	}
	
	# If the url has .pdf
	if url.find('.pdf') != -1:
		# Get the resourse using header
		r = requests.get(url, stream=True, headers=headers)
		# iterate all the content
		with open('/tmp/metadata.pdf', 'wb') as f:
			# Save the content in file that is in temporary folder
			f.write(r.content)
		# Convert .pdf to string
		text = pdf_download('/tmp/metadata.pdf')
		# Return string with policy
		return text
		
	# If the url is a simple html page
	else:
		# Get the resourse using header and add time to load, to bypass bot protection
		r = requests.get(url, verify=False, headers=headers, timeout=3.5)
		# Decode html as spanish content
		r.encoding = 'utf-8'
		
		# Create an html to string converter
		h = html2text.HTML2Text()
		h.ignore_links = True # Ignore links
		h.ignore_images = True # Ignore images
		h.ignore_tables = True # Ignore tables
		# Get text from the html content previusly loaded
		text = h.handle(r.text)
		# Return string with policy
		return text


# Copyright © 2021, 2022 Jaime Ramírez.
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation
