import json
import pandas as pd

data = json.load(open("Subtle Engine.json"))
tags = pd.read_csv("Subtle Engine.csv", index_col="Key")["Manual Tags"].to_dict()

for item in data:
    key = item["id"].split("/")[-1]
    tagged_item = dict(**item, **{"keyword": [t.strip() for t in tags[key].split(";")]})
    with open("Individual JSON/"+key+".json", "w") as f:
        json.dump(tagged_item, f)
