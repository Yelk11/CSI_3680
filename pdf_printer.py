#Output to PDF

#Project

import PyPDF2
import json

pdfWriter = PyPDF2.PdfFileWriter()
for i in range(1):
    pdfWriter.addBlankPage(219, 297)

title = "spaghetti"
instructions = "r4fgfvefjwegfdwvfgjw"
ingredients = ["er4e", "reref", "3ewrfe"]

pdfOutputFile = open('recipe.pdf','wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
