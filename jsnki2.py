import json

person = {"name": "Bob", "lang": ['US', 'PL'], "age": 32, "married": True}

with open('osoba.json', 'w') as json_file:
    json.dump(person, json_file, indent=4)
