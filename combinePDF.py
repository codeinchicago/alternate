#Project: Combining select pages from many PDFs.

#TODO: Check if file overwrites an existing file.

import PyPDF2, os

#Get the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Loop through all pages besides the first and add them.
    #Note that the counting starts at 0, so starting at 1 ignores first page.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#Save the resulting PDF to a file.
pdfOutput = open('allPDF.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

#Further ideas: cut out specific pages from PDFs, reorder pages in a PDF, create PDF from
#only those pages with specific text, identified by extractText().