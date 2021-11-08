from recipe_scrapers import scrape_me
import json, re



def get_recipe(url):
  scraper = scrape_me('https://www.yummly.com'+ url)
  json_obj = {}
  json_obj['name'] = scraper.title()
  json_obj['ingredients'] = scraper.ingredients()
  return json_obj
 
def yummly(category):
  yummly = "https://www.yummly.com/recipes?q=" + category + "&taste-pref-appended=true"
  scraper = scrape_me(yummly)
  
  #grab all links on search page
  link_list = []
  for line in scraper.links():
      link = line.get('href')
      if re.search("/recipe/", link) and link not in link_list:
        link_list.append(link)
  
  recipe_list = {}
  recipe_list['recipe'] = []
  for url in link_list:
    print(url)
    recipe_list['recipe'].append(get_recipe(url))

  
  return json.dumps(recipe_list, indent=4)

# out = yummly('mexican')
# print(type(out))
# print(out)
# with open('out.json', 'w') as f:
#   f.write(out)