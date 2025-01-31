import requests
from bs4 import BeautifulSoup
r=requests.get('https://moxfield.com/decks/public')
soup=soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())
