from recipe_scrapers import scrape_me
import json, re

def get_recipe(url):
  scraper = scrape_me('https://www.yummly.com'+ url)
  print(scraper.title())

def steamyKitchen(category):
  steamyKitchen = "https://www.yummly.com/recipes?q=" + category + "&taste-pref-appended=true"
  scraper = scrape_me(steamyKitchen)
  
  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipe/", link) and link not in link_list:
        link_list.append(link)
  print(link_list)
  
  recipe_list = []
  for url in link_list:
    recipe_list.append(get_recipe(url))
  print(recipe_list)


steamyKitchen('mexican')