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

def getdetails(soup):
    details = []
    for detail in soup.find_all('div', attrs={'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}):
        items = {
            'name': detail.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}).text
        }
        try:
            items['price'] = detail.find(class_='a-offscreen').text
        except:
            items['price'] = ''
            
        details.append(items)
    return details
data = getdata(url)
url = getdetails(data)
print(url)