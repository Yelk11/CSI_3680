#Output to PDF

#Project

import epicurious_scraper as epic
import json
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.add_font("Roboto Slab", '', "RobotoSlab-Regular.ttf", uni=True)

matt = epic.epicurious_scraper("mexican")

recipes = json.loads(matt)


for recipe in recipes["recipe"]:
    pdf.set_font('Roboto Slab', '', 12)
    pdf.cell(0, 10, recipe["name"], ln=True)
    for ingredient in recipe["ingredients"]:
        pdf.set_font('Roboto Slab', '', 10)
        pdf.cell(0, 10, ingredient, ln=True)
    #pdf.multi_cell(0, 10, recipe["directions"])
    pdf.add_page()
    

#METHOD THAT PRINTS JSON as String - Last Resort
#recipesStr = json.dumps(matt)
#pdf.multi_cell(0, 10, recipesStr)

pdf.output('recipes.pdf')
