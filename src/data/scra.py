from requests_html import HTMLSession
from bs4 import BeautifulSoup


s = HTMLSession()

url = 'https://www.amazon.co.uk/s?k=dslr+camera&ref=nb_sb_noss'

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getitemname(soup):
    # this will return all item names
    items = []
    for item in soup.find_all('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}):
        items.append(item.text)
    return items

def getprices(soup):
    # this will return all item names
    prices = []
    for price in soup.find_all('span', attrs={'class': 'a-price'}):
        prices.append(price.find(class_='a-offscreen').text)
    return prices
data = getdata(url)
url = getprices(data)
print(url)