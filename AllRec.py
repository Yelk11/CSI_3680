from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

scraper.title()
scraper.total_time()
scraper.yields()
scraper.ingredients()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available



'''
Input = {
    get_recipe_list(cuisine)
    }
cuisine = {
    Italian,
    Mexican,
    Moroccan,
    French,
    Asian,
    Indian,
    Thai,
    Mediterranean
    }

Name = {
    ingredient and ammount
    }
'''

x = {

  "Name": None,
  "ingredient_list": [
    {"ingredient": "oregeno", "amount": 2, "Unit": "Cups"},
    {"ingredient": "tomatoe paste", "amount": 9, "Unit": "Ounces"},
    {"ingredient": "oregeno", "amount": 2, "Unit": "Cups"},
  ]
}



import json
from recipe_scrapers import scrape_me
import re


# dont call this method!!
def get_recipe(url):
  scraper = scrape_me('https://www.allrecipes.com'+ url)
  
  try:
    print(scraper.title())
  except:
    print("no title found")

  # print(scraper.title())
  # print("hello")
  # x = [
  #   {
  #     "Name": scraper.title(),
  #     "Ingredients":scraper.ingredients()
  #   }
  # ]
  #return x

# Jared, use this method. It will return a JSON object that you pass to Nick
def get_recipe_list(cuisine):
  search_url = "https://www.allrecipes.com/search/?cuisine=" + cuisine + "&content=recipe"
  scraper = scrape_me(search_url)
  
  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipes/food/views/", link) and link not in link_list:
        link_list.append(link)
  
  recipe_list = []
  for url in link_list:
    recipe_list.append(get_recipe(url))
  print(recipe_list)

  #return my_json




# Driver function to test
get_recipe_list("italian")






  
scraper.total_time()
scraper.yields()

scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available
