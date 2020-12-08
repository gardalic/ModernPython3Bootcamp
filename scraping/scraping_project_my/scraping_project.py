import requests
from bs4 import BeautifulSoup
from random import choice

from requests.api import get

class QuoteScraper():
    """Scrapes quotes from http://quotes.toscrape.com/ and returns information on the author."""
    def __init__(self):
        self.quotes = []
        self.url = "http://quotes.toscrape.com/"
        # self.page_ext = "/page/10/"

    def scrape_page(self, url):
        """Scrapes the entire page and returns a response."""
        response = requests.get(url)
        if response.status_code == 200:
            return response


    def get_page_quotes(self, response):
        """Parse quote info and append it to the object attribute. If there are none, returns None."""
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.findAll("div", {"class": "quote"})

        if quotes:
            for quote in quotes:
                quote_info = {
                    "quote": quote.find("span", {"class": "text"}).get_text().strip("“”"), 
                    "author": quote.find("small", {"class": "author"}).get_text(),
                    "author_link": quote.find("a")["href"]
                }
                self.quotes.append(quote_info)
        else: 
            return False


if __name__ == '__main__':
    qs = QuoteScraper()
    response = qs.scrape_page(qs.url)

    if response:
        qs.get_page_quotes(response)
        for quote in qs.quotes:
            print(quote)
