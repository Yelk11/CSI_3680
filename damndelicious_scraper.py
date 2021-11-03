from recipe_scrapers import scrape_me
import json

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://steamykitchen.com/121682-mexican-street-corn-elote-in-the-microwave.html')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
#scraper = scrape_me('https://www.bettycrocker.com/search?term=' + category, wild_mode=True)

print(scraper.title())
scraper.total_time()
scraper.yields()
scraper.ingredients()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available

recipe = {
    "name":scraper.title(),
    "time":str(scraper.total_time()) + ' minutes',
    "yield":scraper.yields(),
    "ingredients":scraper.ingredients(),
    "instructions":scraper.instructions()
}


json_dump = json.dumps(recipe)

print(json_dump)