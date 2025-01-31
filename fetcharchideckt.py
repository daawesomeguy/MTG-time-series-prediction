import requests, json
from bs4 import BeautifulSoup
from functools import reduce
def get_value(data, path):
    keys = path.split(".")
    return reduce(lambda d, key: d[int(key)] if isinstance(d, list) and key.isdigit() else d.get(key, None), keys, data)

def get_links():
    r=requests.get('https://archidekt.com/search/decks?deckFormat=3&orderBy=-updatedAt&page=1')
    soup = BeautifulSoup(r.text)
    script_tag=soup.find_all(class_='deckLink_thumbnail__U3ZsF')
    #print(str(script_tag))
    linklist=[]
    for tag in script_tag:
        if tag and tag.has_attr('href'):
            link = "https://archidekt.com" + tag['href']
        print(link)
        linklist.append(link)
    #print(linklist)
    return linklist
def get_cards(links):
    namelist=[]
    for link in links:
        r=requests.get(link)
        soup = BeautifulSoup(r.text)
        script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
        if script_tag:
            json_data = json.loads(script_tag.string) 
        else:
            print("JSON data not found!")
        result = get_value(json_data, "props.pageProps.redux.deck.cardMap")
        names = [entry["name"] for entry in result.values()if "name" in entry]
        namelist.append(names)
    return namelist



print(get_cards(get_links()))
