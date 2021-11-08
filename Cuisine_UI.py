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
    "Japanese",
    "Indian",
    "Mexican",
    "Italian",
    "Cajun",
    "American"
    ]
#call functions

def web_Select(e):
    if drop_site.get() == "All Recipes":
        webbrowser.open('https://www.allrecipes.com')
    elif drop_site.get() == "Epicurious":
        webbrowser.open('https://www.epicurious.com/')
    elif drop_site.get() == "Damndelicous":
        webbrowser.open('https://damndelicious.net')
        
def style_Select(x):
    if drop_style.get() == "Chinese":
        print("I want Chinese")
    elif drop_style.get() == "Japanese":
        print("I want Japanese")
    elif drop_style.get() == "Indian":
        print("I want Indian")
    elif drop_style.get() == "Mexican":
        print("I want Mexican")
    elif drop_style.get() == "Italian":
        print("I want Italian")
    elif drop_style.get() == "Cajun":
        print("I want Cajun")
    elif drop_style.get() == "American":
        print("I want American")
    
#drop down 1
drop_site = ttk.Combobox(Hungry, value = Websites)
drop_site.pack(pady = 20)

#drop down 2
drop_style = ttk.Combobox(Hungry, value = Flavor)
drop_style.pack(pady = 20)

#bind
drop_site.bind("<<ComboboxSelected>>", web_Select)
drop_style.bind("<<ComboboxSelected>>", style_Select)


Hungry.mainloop()



