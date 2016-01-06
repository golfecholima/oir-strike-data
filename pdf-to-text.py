import os, schedule, time, PyPDF2, re

tmp = '/Users/workmcgerk/Desktop/repos/oir-strike-data/tmp'
pdf_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/PDF/oir-strike-releases-pdf'
txt_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/TXT/oir-strike-releases-txt'
count = []

def job():
	for file in os.listdir(tmp):
		print 'Converting', file,'to text ...' 
		pdf = open(file, 'rb') # read the pdf file
		totpages = PyPDF2.PdfFileReader(pdf).getNumPages()
		print 'This document has', totpages, 'pages'
		raw = PyPDF2.PdfFileReader(pdf).getPage(0).extractText() # read it with PyPDF2, get each page, extract the text
		final = re.sub(r'  ', '\n', re.sub(r'\n', '', raw)) # do some regex to make it more readable
		print 'Here\'s the converted text:\n', final
		# write a file with the converted text and save it in the TXT folder
		# move the original PDF to the PDFs folder

job()