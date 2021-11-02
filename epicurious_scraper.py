

'''
Input:
get_recipe_list(cuisine)
cuisine:
    Italian
    Mexican
    Moroccan
    French
    Asian
    Indian
    Thai
    Mediterranean

Name
    ingredient and ammount

x = {

  "Name": None,
  "ingredient_list": [
    {"ingredient": "oregeno", "amount": 2, "Unit": "Cups"},
    {"ingredient": "tomatoe paste", "amount": 9, "Unit": "Ounces"},
    {"ingredient": "oregeno", "amount": 2, "Unit": "Cups"},
  ]
}

'''

import json

from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)

scraper.title()
scraper.total_time()
scraper.yields()
scraper.ingredients()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available








