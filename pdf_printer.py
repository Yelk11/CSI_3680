#Output to PDF

#Project

import json
import PyPDF2
from fpdf import FPDF
from PyPDF2 import PdfFileReader
from json2html import *
import fitz

def write_to_pdf(input_json):
    pdf = FPDF('P', 'mm', 'A4')

    # setup pdf file
    pdf.add_page()
    pdf.add_font('Roboto', '', 'Roboto-Black.ttf', uni=True)
    pdf.set_font("Roboto", '', 12)

    #Load recipe data from json and output to pdf format
    recipes = json.loads(input_json)
    for recipe in recipes["recipe"]:
        pdf.cell(0, 10, recipe['name'], ln=True)
        for ingredient in recipe["ingredients"]:
            pdf.cell(0, 10, ingredient, ln=True)
        pdf.multi_cell(0, 10, recipe["directions"])
        pdf.add_page()
    pdf.output('recipes.pdf')

    #Scrape PDF
    with fitz.open("recipes.pdf") as doc:
        text = ""
        for page in doc:
            text += page.getText()
            html2=("<h1>Recipes</h1>"+("<p>"+text+"<br>"+"</p>"))
            file = open('recipes.html','w')
            file.write(html2)
        file.close()
