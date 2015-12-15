import PyPDF2

pdfStrikeRelease = open('/path/to/some/pdf', 'rb') 

# rb = read binary

pdfReader = PyPDF2.PdfFileReader(pdfStrikeRelease)
pageObj = pdfReader.getPage(0)
rawText = pageObj.extractText()

# The clean the text by removing all '\n' and adding a return where any double space occurs.

import re

cleanText = re.sub(r'\n', "", rawText)
cleanText = re.sub(r'  ', "\n", cleanText)

