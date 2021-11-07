from recipe_scrapers import scrape_me
import json, re

dictionary=[]
# Data to be written
def get_recipe(url):
    scraper = scrape_me('https://www.allrecipes.com'+ url)
    
    dictionary.append ={
        "name" : scraper.title(),
        "time" : str(scraper.total_time()) + ' minutes',
        "yield" : scraper.yields(),
        "ingredients" : scraper.ingredients(),
        "instructions" : scraper.instructions()
    }
  
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 4)
      
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

def yummly(category):
  yummly = "https://www.yummly.com/recipes?q=" + category + "&taste-pref-appended=true"
  scraper = scrape_me(yummly)
  
  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipe/", link) and link not in link_list:
        link_list.append(link)
  
  dictionary = []
  recipe_list = []
  for url in link_list:
    recipe_list.append(get_recipe(url))

yummly(input('Please enter the type of cuisine you want to search for: '))

