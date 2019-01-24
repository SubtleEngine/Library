import json
import pandas as pd

cover_url = "https://books.google.co.uk/books/content?id={}&printsec=frontcover&img=5&zoom=2"

data = json.load(open("Subtle Engine.json"))
tags = pd.read_csv("Subtle Engine.csv", index_col="Key")["Manual Tags"].to_dict()

new_data = []

for item in data:
    key = item["id"].split("/")[-1]
    item_extra = {}
    item_extra["keyword"] = [t.strip() for t in tags[key].split(";")]
    if "note" in item:
        item_extra["cover"] = cover_url.format(item["note"].split()[-1])
    tagged_item = dict(**item, **item_extra)
    with open("Individual JSON/{}.json".format(key), "w") as f:
        json.dump(tagged_item, f, indent=4)
    new_data.append(tagged_item)

with open("Subtle Engine.json", "w") as f:
        json.dump(new_data, f, indent=4)
