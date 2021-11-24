#Output to HTML and PDF

#Project

import json
import PyPDF2
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


    pdfFileObj = open('recipes.pdf', 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)

    text = pageObj.extractText()

    print(text)

    html2="<p>" +text+ "</p>"
    
    pdfFileObj.close()

    
    
    html="""
    <html>
        <body>
            <h1>Recipes</h1>
            <h2>Name goes here</h2>
                <p> ingredients go here </p>
                <p> instructions go here </p>
        </body>
    </html>
    """

    file = open('recipes.html','w')
    file.write(html2)
    file.close()
