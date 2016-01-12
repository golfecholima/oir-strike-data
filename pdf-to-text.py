import os, schedule, time, PyPDF2, re

tmp = '/Users/workmcgerk/Desktop/repos/oir-strike-data/tmp'
pdf_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/PDF/oir-strike-releases-pdf'
txt_folder = '/Users/workmcgerk/Desktop/repos/oir-strike-data/TXT/oir-strike-releases-txt'
count = []

def job():
	for file in os.listdir(tmp):
		pdfname = file.replace(' ', '-')
		txtname = pdfname.replace('pdf', 'txt')
		print 'Creating', txtname
		txtfile = open(txtname, 'w')
		print '\nConverting', file,'to text ...\n' 
		pdf = open(file, 'rb') # read the pdf file
		totpages = PyPDF2.PdfFileReader(pdf).getNumPages()
		print 'This document has', totpages, 'pages\n'
		for page in PyPDF2.PdfFileReader(pdf).pages: 
			raw = page.extractText() # extract the text of each page
			final = re.sub(r'  ', '\n', re.sub(r'\n', '', raw)) # do some regex to make it more readable
		print 'Here\'s the converted text:\n\n', final
		txtfile.write(final) # write a file with the converted text and save it in the TXT folder
		print 'It\'s now stored in TKTK' # move the original PDF to the PDFs folder
job()