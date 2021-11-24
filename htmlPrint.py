import json


def html_printer(input_json):
    recipes = json.loads(input_json)
    for recipe in recipes["recipe"]:
        html = "<h1>"+recipe['name']+"</h1>"
        for ingredient in recipe["ingredients"]:
            html += "<p>"+ingredient+"</p>"
        html += "<p>"+recipe["directions"]+"</p>"
        file = open("out/"+recipe['name']+".html", "w")
        file.write(html)
        file.close()
