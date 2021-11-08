#Output to PDF

#Project

import epicurious_scraper as epic
import damndelicious_scraper as delicious
import json
from fpdf import FPDF

def write_to_pdf(PDFRecipes):
    pdf = FPDF('P', 'mm', 'A4')

    pdf.add_page()

    pdf.add_font("Roboto Slab", '', "RobotoSlab-Regular.ttf", uni=True)

    pdf.set_font("times", '', 16)

    pdf.cell(0, 10, "Here are some exciting recipes we found on the web!", ln=True)

    pdf.add_page()

    matt = epic.epicurious_scraper("mexican")

    #parker = delicious.yummly("mexican")

    recipes = json.loads(matt)

    #recipes = json.loads(parker)

    for recipe in recipes["recipe"]:
        pdf.set_font('Roboto Slab', '', 12)
        pdf.cell(0, 10, recipe["name"], ln=True)
        for ingredient in recipe["ingredients"]:
            pdf.set_font('Roboto Slab', '', 10)
            pdf.cell(0, 10, ingredient, ln=True)
        #pdf.cell(0, 10, recipe["directions"]) - giving a uni error
        pdf.add_page()

    #recipes = json.loads(parker)

    #for recipe in recipes["recipe"]:
        #pdf.set_font('Roboto Slab', '', 12)
        #pdf.cell(0, 10, recipe["name"], ln=True)
        #for ingredient in recipe["ingredients"]:
            #pdf.set_font('Roboto Slab', '', 10)
            #pdf.cell(0, 10, ingredient, ln=True)
        #pdf.cell(0, 10, recipe["directions"])
        #pdf.add_page()

    pdf.set_font('times', '', 16)

    pdf.multi_cell(0, 10, "Thanks for checking out the exciting recipes we wanted to share with you!", ln=True)

    pdf.output('recipes.pdf')
