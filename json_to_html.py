#Output to HTML and PDF

#Project

import json
import PyPDF2
from json2html import *
from fpdf import FPDF

def write_to_html(input_json):
    
    pdf = FPDF('P', 'mm', 'A4')

    # setup pdf file
    pdf.add_page()
    pdf.add_font('Roboto', '', 'Roboto-Black.ttf', uni=True)
    pdf.set_font("Roboto", '', 12)

    recipes = json.loads(input_json)
    for recipe in recipes["recipe"]:
        pdf.cell(0, 10, recipe['name'], ln=True)
        for ingredient in recipe["ingredients"]:
            pdf.cell(0, 10, ingredient, ln=True)
        pdf.multi_cell(0, 10, recipe["directions"])
        pdf.add_page()
    pdf.output('recipes.pdf')

    infoFromJson = json.loads(jsonfile)
    json2html.convert(json = infoFromJson)
