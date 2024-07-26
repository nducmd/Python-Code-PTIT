import json

with open("flights.json") as file:
    doc = json.load(file)
    
    a = doc["flights"]
    
with open("flights1.json", "w") as file1:
    json.dump(doc, file1, indent = 2)