import PyPDF2

pdfStrikeRelease = open('/path/to/some/pdf', 'rb') 

# rb stands for read binary

pdfReader = PyPDF2.PdfFileReader(pdfStrikeRelease)
pageObj = pdfReader.getPage(0)
rawText = pageObj.extractText()

# The clean the text by removing all '\n' and adding a return where any double space occurs.

import re

cleanText = re.sub(r'\n', "", rawText)
finalText = re.sub(r'  ', "\n", cleanText)

# Can all be simplified down to

release = open('/path/to/pdf.pdf', 'rb')

rawText = PyPDF2.PdfFileReader(release).getPage(0).extractText()

finalText = re.sub(r'  ', "\n", re.sub(r'\n', "", rawText))

print(finalText)

# OR

print(re.sub(r'  ', "\n", re.sub(r'\n', "", PyPDF2.PdfFileReader(open('/path/to/pdf.pdf', 'rb')).getPage(0).extractText())))

# OOF

### Regexes ###

# For more recent files ...

# Find the release number: 

releaseNumber = re.findall(r'(?<=Release # )([\d]{8}-?\d?\d?)', finalText)

# Find the date and give it in coding friendly format:

date = re.findall(r'\w+ (\d\d?, \d\d\d?\d?)', finalText)

# Find the location where the strike took place

location = re.findall(r'(?<=Near )(.+?)(?=,)', finalText)

if os.path.isfile(pdf_folder)



***


outputs = glob.glob('TXT/*.txt')
inputs = glob.glob('*/*/*.pdf')



for file in glob.glob('*/*/*.pdf'):
	print 'Converting ', file, ' to .txt ...'

***

# This converts a file in tmp dir from PDF to txt and prints it

import os, schedule, time, PyPDF2, re

tmp = '/Users/workmcgerk/Desktop/repos/oir-strike-data/tmp'
pdf_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/PDF/oir-strike-releases-pdf'
txt_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/TXT/oir-strike-releases-txt'
count = []

def job():
	for file in os.listdir(tmp):
		print '\nConverting', file,'to text ...\n' 
		pdf = open(file, 'rb') # read the pdf file
		totpages = PyPDF2.PdfFileReader(pdf).getNumPages()
		print 'This document has', totpages, 'pages\n'
		for page in PyPDF2.PdfFileReader(pdf).pages: 
			raw = page.extractText() # extract the text of each page
			final = re.sub(r'  ', '\n', re.sub(r'\n', '', raw)) # do some regex to make it more readable
		print 'Here\'s the converted text:\n\n', final
		# write a file with the converted text and save it in the TXT folder
		print 'It\'s now stored in', TKTK,
		# move the original PDF to the PDFs folder
job()