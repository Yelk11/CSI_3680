#Output to PDF

#Project

import json
from fpdf import FPDF

title = "spaghetti"
instructions = "r4fgfvefjwegfdwvfgjw"
ingredients = ["er4e", "reref", "3ewrfe"]
pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('times', '', 14)

pdf.cell(40, 10, title)

pdf.output('recipes.pdf')
