import requests
from bs4 import BeautifulSoup
import os
__all__ = ["Product_Scraper"]



class Product_Scraper:
    """
    Data mining/web scraping bot to generate relevant leads/accounts from SkimLink Websites
    """

    def __init__(
        self,
        website: str,
        filter: list,
        search_term: str,
        headers: str,
        seperate: bool

    ):
        """
        Initializes Scraper
        :param company: which website to search
        :param to_ignore: keywords to filter out websites and URLs
        """
        self.website = website
        self.filter = [word.lower() for word in filter]
        self.search_term = search_term
        self.headers = headers
        self.seperate = seperate
        d = os.path.dirname(__file__) # directory of script
        if(seperate):
            title_path = r'{}/Product Title.csv'.format(d)
            self.f = open(title_path, 'w')
            headers = 'Title \n'
            self.f.write(headers)

            filename = 'Product URL.csv'
            URL_path = r'{}/Product URL.csv'.format(d)
            self.f2 = open(URL_path, 'w')
            headers = 'URL \n'
            self.f2.write(headers)
        
        else:
            title_path = r'{}/Products.csv'.format(d)
            self.f = open(title_path, 'w')
            headers = 'Title, URL \n'
            self.f.write(headers)       
    
    """
    Runs script to generate relevant products from the SkimLink websites
    """
    
    def run(self):
        if self.website == '1': 
            site = 'https://www.zazzle.com/s/'
        elif self.website == '2':
            site = 'https://www.cardsdirect.com/search.aspx?keywords='
        elif self.website == '3':
            site = 'https://www.amazon.com/s?k=%5B%5D'
        else:
            raise SyntaxError('If you do not type 1,2, or 3, then you must restart program')       
        URL = site + self.search_term
        
        page = requests.get(URL, headers=self.headers)
        ## returns a html block and declares files 
        soup = BeautifulSoup(page.content, "lxml")

        
        ## Zazzle search term condition
        if self.website == '1':
            search_items = soup.find_all('div', class_="SearchResultsGridCell-realviewContainer")
            for link in search_items:
                URL = link.find('a')['href']
                title = link.find('a')['aria-label']
                title = title[8:] # getting rid of "product: "
                if(self.product_filter(title) != True):
                    self.file_write(title,URL)
            if(self.seperate):
                self.f.close()
                self.f2.close()
            else:
                self.f.close()               

        ## Cardsdirect search term condition
        if self.website == '2':
            search_items =soup.find_all('div', class_="product-info")
            for link in search_items:
                temp = link.find('a')
                if temp is not None:
                    if(self.product_filter(title) != True):
                        self.f2.write('https://www.cardsdirect.com/' + temp['href'] + '\n')
                        self.f.write(temp['title'] + '\n')
            if(self.seperate):
                self.f.close()
                self.f2.close()
            else:
                self.f.close()

        ## Amazon search term condition
        if self.website == '3':
            search_items = soup.find_all('div', class_="a-section a-spacing-medium")
            for link in search_items:
                URL = link.find('a')['href']
                title = link.find('span', class_= 'a-size-base-plus a-color-base a-text-normal')
                if title is not None:
                    if(self.product_filter(title) != True):
                        self.f.write(title.text + '\n')
                        self.f2.write('https://www.amazon.com'+URL + '\n')
            if(self.seperate):
                self.f.close()
                self.f2.close()
            else:
                self.f.close()
    
    
    ## Filters out products using the words included by the client 
    
    def product_filter(self, product_title):
        for word in self.filter:
            if product_title.lower().find(word) == -1:
                return False
        return True

    ## Prints out products into one or two files depending on the clients choice
    def file_write(self, product_title, product_URL):
        if(self.seperate):
            self.f.write(product_title + '\n')
            self.f2.write(product_URL + '\n')
        else:
            self.f.write(product_title + ', ' + product_URL +  '\n')                  