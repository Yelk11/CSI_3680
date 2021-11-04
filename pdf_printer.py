#Output to PDF

#Project

import json
from fpdf import FPDF

title = "Spaghetti"
instructions = "Break noodles down to correct size. Add noodles to pot and pour water..."
ingredients = ["Noodles(any kind)", "water", "cheese"]

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('times', '', 14)

pdf.cell(40, 10, title, ln=True)

pdf.cell(40, 10, instructions, ln=True)

pdf.cell(40, 10, ingredients[0], ln=True)

pdf.cell(40, 10, ingredients[1], ln=True)

pdf.cell(40, 10, ingredients[2])


pdf.output('recipes.pdf')
