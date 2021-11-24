#imports 
import webbrowser,sys,pyperclip
import requests,bs4
from tkinter import *
from tkinter import ttk
import epicurious_scraper as epic
import yummly_scraper as delicious
import pdf_printer as pdf
import htmlPrint

#UI text
print('Get Cooking.....')

Hungry = Tk()
Hungry.title('Recipe Scraper')
Hungry.geometry("500x400")

Websites = [
    "Epicurious",
    "Yummly"
    ]


drop_site = ttk.Combobox(Hungry, value = Websites)
drop_site.pack(pady = 20)

drop_style = ttk.Combobox(Hungry)
drop_style.pack(pady = 20)


def web_Select(x):
    if drop_site.get() == "Epicurious":
        drop_style['value'] = epic.get_cuisines()
    elif drop_site.get() == "Yummly":
        drop_style['value'] = delicious.get_cuisines()

def style_Select(x):
    if drop_site.get() == "Epicurious":
        print('Pdf writer started...')
      #  pdf.write_to_pdf(epic.epicurious_scraper(drop_style.get()))
        htmlPrint.html_printer(epic.epicurious_scraper(drop_style.get()))
        print('PDF printed')
    elif drop_site.get() == "Yummly":
        print('Pdf writer started...')
        pdf.write_to_pdf(delicious.yummly(drop_style.get()))
        print('PDF printed!')

#bind
drop_site.bind("<<ComboboxSelected>>", web_Select)
drop_style.bind("<<ComboboxSelected>>", style_Select)


Hungry.mainloop()










