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

def do_it(url):
  url_list = grab_all_links(url)
  json_obj = {'larry':0}
  json_list = []
  for item in url_list:
    json_list.append(scrape_page(url+item))
  print(json_list)
  for item in json_list:
    

do_it(url)


