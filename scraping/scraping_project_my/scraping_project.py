import requests
from bs4 import BeautifulSoup
from random import choice, randint
from requests.api import get


class QuoteScraper:
    """Scrapes quotes from http://quotes.toscrape.com/ and returns information on the author."""

    def __init__(self):
        self.quotes = []
        self.url = "http://quotes.toscrape.com"
        self.author_bio = ""
        self.hints = []

    def get_response(self, url):
        """Returns a response for the given URL."""
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
                    "quote": quote.find("span", {"class": "text"})
                    .get_text()
                    .strip("“”"),
                    "author": quote.find("small", {"class": "author"}).get_text(),
                    "author_link": quote.find("a")["href"],
                }
                self.quotes.append(quote_info)
            return True  # To return the flag for the loop later
        else:
            return False

    def scrape_site(self):
        """Scrape the site page by page. Works by incrementing pages while it gets at least one quote."""
        # Get initial page
        flag = self.get_page_quotes(self.get_response(self.url))
        pg_number = 2
        while flag:
            flag = self.get_page_quotes(
                self.get_response(f"{self.url}/page/{pg_number}/")
            )
            pg_number += 1

    def get_author_bio(self, url):
        """Make request to the author page and get birth date and location."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        autor_info = soup.find("div", {"class": "author-details"})

        born_date = autor_info.find("span", {"class": "author-born-date"}).get_text()
        born_location = autor_info.find(
            "span", {"class": "author-born-location"}
        ).get_text()
        return f"{born_date} in {born_location}"  # Moved parsing out of return, more readable this way

    def generate_hint(self, author_name):
        """Generate hint list."""
        split_name = author_name.split()

        self.hints.append(f"Their first name starts with {split_name[0][:1]}")
        self.hints.append(f"Their last name starts with {split_name[-1][:1]}")
        if len(split_name) > 2:
            self.hints.append("They have a middle name")
        if "." in author_name:
            self.hints.append("The name is initialized")
        if len(split_name) == 2 and "." not in author_name:
            self.hints.append(
                "They don't have a middle name and the name is not initialized"
            )
        self.hints.append(f"The last name length is {len(split_name[-1])}")
        self.hints.append(f"The first name length is {len(split_name[0])}")

    def game_loop(self):
        """Run the main loop. Give a quote and ask for 4 guesses. After each game, ask for new game."""
        new_game = "y"
        while new_game.lower() == "y":
            quote = choice(self.quotes)
            self.author_bio = self.get_author_bio(f"{self.url}{quote['author_link']}")
            self.generate_hint(quote["author"])
            guess_no = 4

            print(f"Who said: {quote['quote']}")
            while True:
                user_input = input()
                if user_input.lower() == quote["author"].lower():
                    print(f"Great! You guessed the author in {5 - guess_no} attempts!")
                    break
                else:
                    guess_no -= 1
                    if guess_no > 0:
                        print(
                            f"Guess again (guesses left: {guess_no})! Hint: {self.hints.pop(randint(0, len(self.hints) - 1))}"
                        )
                    else:
                        print(f"You used up all your guesses...")
                        break
            new_game = input("Do you want to play again (y/n)? ")


if __name__ == "__main__":
    qs = QuoteScraper()
    qs.scrape_site()
    qs.game_loop()
