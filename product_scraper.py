import requests
from bs4 import BeautifulSoup


## Initlaizes url and search terms

website = input('Enter (1,2 or,3) for Zazzle, Cardsdirect, or Amazon \n')
if website == '1': 
    site = 'https://www.zazzle.com/s/'
elif website == '2':
    site = 'https://www.cardsdirect.com/search.aspx?keywords='
elif website == '3':
    site = 'https://www.amazon.com/s?k=%5B%5D'
else:
    raise SyntaxError('If you do not type 1,2, or 3, then you must restart program')

search_term = input('Enter search term \n')
URL = site + search_term
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36', 
                           'Accept-Language': 'en-US, en;q=0.5' }
page = requests.get(URL, headers=headers)

## returns a html block and declares files 
soup = BeautifulSoup(page.content, "lxml")
filename = 'Product Title.csv'
f = open(filename, 'w')
headers = 'Title \n'
f.write(headers)

filename = 'Product URL.csv'
f2 = open(filename, 'w')
headers = 'URL \n'
f2.write(headers)

## Zazzle search term condition
if website == '1':
    search_items = soup.find_all('div', class_="SearchResultsGridCell-realviewContainer")
    for link in search_items:
        URL = link.find('a')['href']
        title = link.find('a')['aria-label']
        title = title[8:] # getting rid of "product: "
        f.write(title + '\n')
        f2.write(URL + '\n')
    f.close()
    f2.close()


## Cardsdirect search term condition
if website == '2':
    search_items =soup.find_all('div', class_="product-info")

    for link in search_items:
        temp = link.find('a')
        if temp is not None:
            f2.write('https://www.cardsdirect.com/' + temp['href'] + '\n')
            f.write(temp['title'] + '\n')
    f.close()
    f2.close()

## Amazon search term condition
if website == '3':
    search_items = soup.find_all('div', class_="a-section a-spacing-medium")
    for link in search_items:
        URL = link.find('a')['href']
        title = link.find('span', class_= 'a-size-base-plus a-color-base a-text-normal')
        if title is not None:
            f.write(title.text + '\n')
            f2.write('https://www.amazon.com'+URL + '\n')
    f.close()
    f2.close() 