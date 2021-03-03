from Product_Scraper import Product_Scraper


def main():
    
    ## 1 = Zazzle, 2 = CardsDirect, 3 = Amazon
    website = "1"
    filter = ["Notes"]
    search_term = "Thank You Cards"
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36', 
                           'Accept-Language': 'en-US, en;q=0.5' }
    seperate = True

    scraper = Product_Scraper(
        website = website,
        filter = filter,
        search_term = search_term,
        headers = headers,
        seperate = seperate
    )
    scraper.run()


if __name__ == "__main__":
    main()