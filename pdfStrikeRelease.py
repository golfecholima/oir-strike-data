import PyPDF2

pdfStrikeRelease = open('/path/to/some/pdf', 'rb') 

# rb = read binary

pdfReader = PyPDF2.PdfFileReader(pdfStrikeRelease)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# The clean the text by removing all '\n' and adding a return where any double space occurs.
