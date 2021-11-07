#Output to PDF

#Project

import json
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('times', '', 14)

with open('example.json') as f:
    recipes = json.load(f)

recipesStr = json.dumps(recipes)

pdf.multi_cell(0, 10, recipesStr)

pdf.output('recipes.pdf')
