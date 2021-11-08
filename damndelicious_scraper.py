from recipe_scrapers import scrape_me
import json, re

aJson= {}
json_data = []
def get_recipe(url):
  scraper = scrape_me('https://www.yummly.com'+ url)
  json_data.append({
      "name":scraper.title(),
      "ingredients":scraper.ingredients(),
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

  aJson = json.dumps(json_data)
  return json.dumps(aJson, indent=4)

yummly('mexican')