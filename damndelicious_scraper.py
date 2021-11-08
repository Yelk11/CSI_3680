from recipe_scrapers import scrape_me
import json, re

json=[]
def get_recipe(url):
  scraper = scrape_me('https://www.yummly.com'+ url)
  json.append({
      "name":scraper.title(),
      "time":str(scraper.total_time()) + ' minutes',
      "yield":scraper.yields(),
      "ingredients":scraper.ingredients(),
      "instructions":scraper.instructions()
    })
  

def yummly(category):
  yummly = "https://www.yummly.com/recipes?q=" + category + "&taste-pref-appended=true"
  scraper = scrape_me(yummly)
  
  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipe/", link) and link not in link_list:
        link_list.append(link)
  
  recipe_list = []
  for url in link_list:
    recipe_list.append(get_recipe(url))

  return json

