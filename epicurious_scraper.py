import requests
from bs4 import BeautifulSoup
import re
import json




def grab_all_links(url):
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'html.parser')
  urls = []
  for link in soup.find_all('a'):
    a_link = link.get('href')
    try:
      if bool(re.search('/recipes/food/views/',a_link)) and a_link not in urls:
        urls.append(a_link)
    except:
      print("Link not found")
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
  return json_obj

def epicurious_scraper(cuisine):
  url = 'https://www.epicurious.com/search/?cuisine=' + cuisine
  url_list = grab_all_links(str(url))
  total = {}
  total['recipe'] = []
  for item in url_list:
    json_obj = scrape_page(url+item)
    total['recipe'].append(json_obj)
  with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(total, f, ensure_ascii=False, indent=4)
    
def get_cuisines():
  cuisine = [
    "italian",
    "mexican",
    "moroccan",
    "french",
    "asian",
    "indian",
    "thai",
    "mediterranean"
  ]
  return cuisine
epicurious_scraper("italian")


