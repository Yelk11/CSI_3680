#imports 
import webbrowser,sys,pyperclip
import requests,bs4
from tkinter import *
from tkinter import ttk
import epicurious_scraper as epic
import damndelicious_scraper as delicious
import pdf_printer as pdf

#UI text
print('Get Cooking.....')

root = Tk()
root.title('Recipe Scraper')
root.geometry("500x400")
#lists
Websites = [
    "All Recipes",
    "Epicurious",
    "Damndelicous"
    ]


drop_site = ttk.Combobox(root, value = Websites)
drop_site.pack(pady = 20)

drop_style = ttk.Combobox(root)
drop_style.pack(pady = 20)


def web_Select(e):
    if drop_site.get() == "All Recipes":
        pass
    elif drop_site.get() == "Epicurious":
        drop_style['value'] = epic.get_cuisines()
    elif drop_site.get() == "Damndelicous":
        drop_style['value'] = delicious.get_cuisines()




def style_Select(x):
    if drop_site.get() == "All Recipes":
        pass
    elif drop_site.get() == "Epicurious":
        pdf.write_to_pdf(epic.epicurious_scraper(drop_style.get()))
        print('done')
    elif drop_site.get() == "Damndelicous":
        pdf.write_to_pdf(delicious.get_recipe(drop_style.get()))
        print('done')




#bind
drop_site.bind("<<ComboboxSelected>>", web_Select)


root.mainloop()



