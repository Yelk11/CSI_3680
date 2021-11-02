

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
import re




def get_recipe_list(cuisine):
  search_url = "https://www.epicurious.com/search/?cuisine=" + cuisine + "&content=recipe"
  scraper = scrape_me(search_url)

  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipes/food/views/", link) and link not in link_list:
        link_list.append(link)
  
  

get_recipe_list("italian")
