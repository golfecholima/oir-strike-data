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

