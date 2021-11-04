import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.epicurious.com'




def grab_all_links(url):
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'html.parser')
  urls = []
  for link in soup.find_all('a'):
    a_link = link.get('href')
    if bool(re.search('/recipes/food/views/',a_link)) and a_link not in urls:
      urls.append(a_link)
  return urls



def scrape_page(url):
  # get html
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'html.parser')

  data = json.loads(soup.find('script', type='application/ld+json').text)

  directions = []
  for line in data['recipeInstructions']:
    directions.append(line['text'])
  json_obj = {}
  json_obj['name'] = data['name']
  json_obj['ingredients'] = data['recipeIngredient']
  json_obj['directions'] = directions
  return json.dumps(json_obj)


'''
{
   "name":"Gluten-Free Fresh Pasta",
   "ingredients":[
      "1 cup gluten-free flour blend (such as Bob\u2019s Red Mill Gluten Free 1-to-1 Baking Flour)",
      "\u00be cup chickpea flour",
      "1 tsp. Diamond Crystal or \u00bd tsp. Morton kosher salt",
      "3 large eggs",
      "2 Tbsp. extra-virgin olive oil"
   ],
   "directions":[
      "Whisk together gluten-free flour blend, chickpea flour, and salt in a large bowl. Whisk eggs and oil in a small bowl to combine.",
      "Add egg mixture to dry ingredients and stir with a fork to incorporate; mixture will be crumbly. Tip out onto a surface and knead until a smooth dough forms, about 3 minutes. Form dough into a ball and wrap tightly in plastic. Chill at least 1 hour and up to 1 day to allow flour to hydrate (the longer you can let it rest, the better).",
      "Roll out pasta according to pasta machine directions or roll out and cut by hand."
   ]
}
'''

print(scrape_page('https://www.epicurious.com/recipes/food/views/gluten-free-fresh-pasta'))


grab_all_links(url)