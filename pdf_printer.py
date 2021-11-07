#Output to PDF

#Project

import epicurious_scraper as epic
import json
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('times', '', 12)

matt = epic.epicurious_scraper("mexican")

recipes = json.loads(matt)


#for recipe in recipes["recipe"]:
    #pdf.cell(0, 10, recipe["name"], ln=True)
    #for ingredient in recipe["ingredients"]:
        #print(ingredient)
        #pdf.cell(0, 10, ingredientStr, ln=True)
    #print(recipe["directions"])
    #pdf.multi_cell(0, 10, recipe["directions"][0])
    

#METHOD THAT PRINTS JSON as String
recipesStr = json.dumps(matt)

pdf.multi_cell(0, 10, recipesStr)

pdf.output('recipes.pdf')
