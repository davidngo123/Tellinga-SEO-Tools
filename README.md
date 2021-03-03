# Linkedin Sales Scraper
**Tellinga SEO Tools** is a webscrapping bot that will find relevant information products from Zazzle, Cardsdirect, and Amazon. (Websites used with skimlinks for Tellinga.com

## Dependencies
*Requires Python 3.7 or later*

[Requests](https://pypi.org/project/requests/), 
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/),

Installation Instructions
` $pip install Requests`
` $pip install bs4`

## Features and Options

`Product_Scraper`: 
- Scrapes Zazzle, Cardsdirect, and Amazon for data on title as well as links

- Choose the website by using  `1, 2, or 3` 
  
  - 1 is Zazzle.com
  - 2 is Cardsdirect.com
  - 3 is Amazon.com
- Search terms will be chosen by the client 
- Run; results saved to Products.csv or (Product Title and Product URL)

`seperate`: 

- Seperate will either print data into one file (products) or seperate data into individual options
- default is set to True 

`filter`:

- Filter doesn't print out titles that includes whatever words the user doesn't want
- E.g. `filter` = ['notes', 'work', 'home'] -> will not print any product with those keywords in the title


## Usage

Fork or clone and set your options and then run main

## Author

* **David Ngo**
