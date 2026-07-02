import json

with open("results.json") as f:
    data = json.load(f)

print(data)