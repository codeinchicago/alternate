#Project: Combining select pages from many PDFs.

#TODO: Check if file overwrites an existing file.

#Further ideas: XXcut out specific pages from PDFs, XXreorder pages in a PDF, XXcreate PDF from only those pages with specific text, identified by extractText().

#Regex search idea in chapter 8.


def combine():
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
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #Save the resulting PDF to a file.
    pdfOutput = open('allPDF3.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

def cutout():
    import PyPDF2, os
    #Cut out pages from PDFs:

    #Get the PDF filenames.
    pdfFiles = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)

    good = False

    cutStart = int(input("What is the start page to remove? "))
    cutEnd = int(input("What is the end page to remove? "))
    # if type(cutStart) == int and type(cutEnd) == int:
    #     good = True

    pdfWriter = PyPDF2.PdfFileWriter()

    #Loop through all the PDF files.
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #Loop through all pages besides the first and add them.
        #Note that the counting starts at 0, so starting at 1 ignores first page.
        
        #Getting from start to beginning of removed pages
        for pageNum in range(0, cutStart):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)        

        #From end of removed pages to end of file
        for pageNum in range(cutEnd-1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #Save the resulting PDF to a file.
    pdfOutput = open('allPDF.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

def reorder():
    #Reordering pages in a PDF

    import PyPDF2, os

    first, last = int(input("Enter first and last numbers to rearrange. ")).split()
    destination = int(input("What page should they be inserted before? "))

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
        #Loop through all pages and add them.

        #Part before rearrange
        for pageNum in range(0, first):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        #Rearranged part
        for pageNum in range(first-1, last+1):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        #Part after rearrange
        for pageNum in range(destination-1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #Save the resulting PDF to a file.
    pdfOutput = open('allPDF.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

def specificText():
    #create a PDF from only those pages with specific text, identified by extractText().
    import PyPDF2, os

    specific = input("What text should the PDFs filter for? ")

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
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            #Checking for the phrase, adding it to the PDF if found
            if specific in pageObj.extractText():
                pdfWriter.addPage(pageObj)

    #Save the resulting PDF to a file.
    pdfOutput = open('allPDF.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

print("Welcome to the PDF manipulator.")
print("Would you like to 1.Combine PDFs\n2.Cut out pages from PDFs.\n3.Rearrange pages\n4.Filter PDFs based on text.")
choice = input("Enter the number of your choice. ")
if int(choice) == 1:
    combine()
if int(choice) == 2:
    cutout()
if int(choice) == 3:
    reorder()
if int(choice) == 4:
    specificText()