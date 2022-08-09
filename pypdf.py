#TODO:
#Need to ask if overriding a file.
#GUI w/ Tkinter

#Initial demonstration

# import PyPDF2 as pdf

# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = pdf.PdfReader(pdfFileObj)

# print(pdfReader.numPages)

# pageObj = pdfReader.getPage(0)

# print(pageObj.extractText())


#Add into TKinter



#Merging PDFs

# import PyPDF2 as pdf

# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')

# pdf1Reader = pdf.PdfFileReader(pdf1File)
# pdf2Reader = pdf.PdfFileReader(pdf2File)

# pdfWriter = pdf.PdfFileWriter()

# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)


# pdfOutputFile = open('combo.pdf', 'wb')

# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()


#Rotating Pages
# import PyPDF2 as pp
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = pp.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateClockwise(90)
# pdfWriter = pp.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile=open('rotatedPage.pdf','wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()


#Overlaying Pages
# import PyPDF2 as pp
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = pp.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)
# pdfWatermarkReader = pp.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# pdfWriter = pp.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)

# for pageNum in range(1,pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# resultPdfFile = open('watermarkedCover.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# minutesFile.close()
# resultPdfFile.close()

print("Test.")