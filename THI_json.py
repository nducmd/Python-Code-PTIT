import json
with open("flights.json") as file:
    doc_json = json.load(file)
    a = doc_json["flights"]
    
t = int(input())
while t > 0:
    t -= 1
    x, y = input().split()
    sum = 0
    for i in a:
        if i["year"] == x:
            sum += int(i["passengers"])
    print(sum)