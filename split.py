import json

data = json.load(open("Subtle Engine.json"))
for item in data:
    key = item["id"].split("/")[-1]
    with open("Individual JSON/"+key+".json", "w") as f:
        json.dump(item, f)
