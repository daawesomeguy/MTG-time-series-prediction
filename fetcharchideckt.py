import requests
from bs4 import BeautifulSoup
r=requests.get('https://archidekt.com/decks/11143456/history_matter')
soup=soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

