import requests
from bs4 import BeautifulSoup
import re, json
r=requests.get('https://archidekt.com/decks/10260015/621_wtf_are_you_doing')
soup = BeautifulSoup(r.text)
print(soup)
#pattern = r'"name":\s*"([^"]+)"'
#matches = re.findall(pattern, r.text)

#if matches:
 #   print(len(matches))
#    #print("Matches:", matches)
script_tag = soup.find("script", {"id": "__NEXT_DATA__"})

if script_tag:
    json_data = json.loads(script_tag.string)  # Convert to Python dict
    #print(json.dumps(json_data, indent=4))  # Pretty print JSON
else:
    print("JSON data not found!")
from functools import reduce

# Function to extract a nested value
def get_value(data, path):
    keys = path.split(".")
    return reduce(lambda d, key: d[int(key)] if isinstance(d, list) and key.isdigit() else d.get(key, None), keys, data)

# Example Usage
result = get_value(json_data, "props.pageProps.redux.deck.cardMap")
#print(result)
names = [entry["name"] for entry in result.values()if "name" in entry]

print(names)
#with open('text.txt','w') as file:
#    file.write(soup.prettify())
