#imports 
import webbrowser,sys,pyperclip
import requests,bs4
from tkinter import *
from tkinter import ttk

#UI text
print('Get Cooking.....')

Hungry = Tk()
Hungry.title('Recipe Scraper')
Hungry.geometry("500x400")
#lists
Websites = [
    "All Recipes",
    "Epicurious",
    "Damndelicous"
    ]

Flavor = [
    "Chinese",
    "Thai",
    "indian",
    "Mexican",
    "Italian",
    "Southern",
    "American"
    ]
#call functions



#drop down 1
drop_site = ttk.Combobox(Hungry, value = Websites)
drop_site.pack(pady = 20)

#drop down 2
drop_style = ttk.Combobox(Hungry, value = Flavor)
drop_style.pack(pady = 20)

#bind
drop_site.bind("<<ComboboxSelected>>", web_Select)
drop_style.bind("<<ComboboxSelected>>", web_Select)


Hungry.mainloop()



