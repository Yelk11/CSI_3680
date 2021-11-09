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
    if a_link != None and a_link not in urls and bool(re.search('/recipes/food/views/',a_link)):
      urls.append(a_link)

  return urls



def scrape_page(url):
  # get html
  reqs = requests.get(url)
  soup = BeautifulSoup(reqs.text, 'html.parser')
  
  text = soup.find("script",type="application/ld+json", text=True)
  data = json.loads(text.contents[0])
  
  directions = ''
  
  for line in data['recipeInstructions']:
    directions += line['text']
  json_obj = {}
  json_obj['name'] = data['name']
  json_obj['ingredients'] = data['recipeIngredient']
  json_obj['directions'] = directions
  return json_obj



def epicurious_scraper(cuisine):
  url = 'https://www.epicurious.com/search/?cuisine=' + cuisine
  base_url = 'https://www.epicurious.com'
  url_list = grab_all_links(str(url))
  total = {}
  total['recipe'] = []
  for item in url_list:
    json_obj = scrape_page(base_url+item)
    total['recipe'].append(json_obj)
  # dump json to file if needed
  # with open('data.json', 'w', encoding='utf-8') as f:
  #   json.dump(total, f, ensure_ascii=False, indent=4)
  return json.dumps(total, indent=4).encode('latin-1')


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


epicurious_scraper('mexican')