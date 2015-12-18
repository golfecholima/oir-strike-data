import PyPDF2

pdfStrikeRelease = open('/path/to/some/pdf', 'rb') 

# rb = read binary

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

print (finalText)

# OR

print (re.sub(r'  ', "\n", re.sub(r'\n', "", PyPDF2.PdfFileReader(open('/path/to/pdf.pdf', 'rb')).getPage(0).extractText())))

# OOF