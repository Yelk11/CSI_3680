#imports 
import webbrowser,sys,pyperclip
import requests,bs4
from tkinter import*

#UI text
print('Get Cooking.....')

Websites = [
    "All Recipes",
    "Epicurious",
    "Damndelicous"
    ]

Hungry = Tk()

food = StringVar(Hungry)
food.set(Websites[0])

s = OptionMenu(Hungry, food, *Websites)
s.pack()

mainloop()






#call function for recipe websites



