import requests

url = requests.get("http://books.toscrape.com/")

response = requests.get(url)

page = response.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')

inTheMain = soup.find('ol', id="row")

title = inTheMain.find-all('li')

for n in title :
    print(n.get_text())
    links = n.find_all('a')
    for l in links:
        print(link['href'])
        print()