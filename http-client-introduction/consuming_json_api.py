import requests

r = requests.get("http://astral.hacksoft.io/api/airline/?format=json")
r = r.json()
r2 = requests.get("http://data.okfn.org/data/core/country-list/r/data.json")
r2 = r2.json()
histogram = {}
all_airports = {}

for item in r2:
    all_airports[item["Name"]] = 0

for el in r:
    for item in r2:
        if el['country_code'] == item['Code']:
            all_airports[item['Name']] += 1

print(all_airports)
