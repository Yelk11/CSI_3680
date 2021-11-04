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
  title = data['name']
  ingredient_list = data['recipeIngredient']
  directions = []
  for line in data['recipeInstructions']:
    directions.append(line)
  
  
  
  # with open("output1.html", "w",encoding="utf-8") as file:
  #   file.write(str(soup))
  # file.close()





scrape_page('https://www.epicurious.com/recipes/food/views/gluten-free-fresh-pasta')


grab_all_links(url)