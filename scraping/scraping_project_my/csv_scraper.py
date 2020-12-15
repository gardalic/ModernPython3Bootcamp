import csv
from os import write
import requests
from bs4 import BeautifulSoup
from requests.api import get
from time import sleep
from csv import DictWriter


class QuoteScraper:
    """Scrapes quotes from http://quotes.toscrape.com/ and returns information on the author."""

    def __init__(self):
        self.quotes = []
        self.url = "http://quotes.toscrape.com"
        # self.hints = []

    def scrape_page(self, response):
        """Parse quote info and append it to the object attribute. If there are none, returns None."""
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.findAll(class_="quote")

        if quotes:
            for quote in quotes:
                quote_info = {
                    "quote": quote.find(class_="text").get_text().strip("“”"),
                    "author": quote.find(class_="author").get_text(),
                    "author_born": self.scrape_author(
                        f"{self.url}/{quote.find('a')['href']}"
                    ),
                }
                self.quotes.append(quote_info)
            return True # return only if quotes were found

    def scrape_site(self):
        """Scrape the site page by page. Works by incrementing pages while it gets at least one quote."""
        # Get initial page
        flag = self.scrape_page(requests.get(self.url))
        pg_number = 2
        while flag:
            flag = self.scrape_page(requests.get(f"{self.url}/page/{pg_number}/"))
            print(f"Scraping {self.url}/page/{pg_number}/...")
            pg_number += 1
            # if flag: sleep(randint(1, 3))

    def scrape_author(self, url):
        """Make request to the author page and get birth date and location."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        autor_info = soup.find(class_="author-details")

        born_date = autor_info.find(class_="author-born-date").get_text()
        born_location = autor_info.find(class_="author-born-location").get_text()
        return f"{born_date} {born_location}"  # Moved parsing out of return, more readable this way

    def make_csv(self):
        """Write all the quotes to a CSV in the same location as the script."""
        filepath = "./quotes.csv"
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            headers = ["quote", "author", "author_born"]
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for quote in self.quotes:
                writer.writerow(quote)


if __name__ == "__main__":
    qs = QuoteScraper()
    qs.scrape_site()
    qs.make_csv()