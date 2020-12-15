from random import choice, randint
from csv_scraper import QuoteScraper
from csv import DictReader


class QuoteGame:
    """Run a guessing game using quotes from the QuoteScrapper class."""

    def __init__(self):
        self.quotes = []

    def get_quotes(self):
        """Get the list of quotes from a CSV."""
        filepath = "./quotes.csv"
        with open(filepath, newline="", encoding="utf-8") as f:
            csv_reader = DictReader(f)
            self.quotes = list(csv_reader)  # DictReader returns OrderedDict, not list

    def generate_hints(self, author_name):
        """Generate hint list."""
        split_name = author_name.split(" ")
        hints = []

        hints.append(f"Their first name starts with {split_name[0][0]}")
        hints.append(f"Their last name starts with {split_name[-1][0]}")
        if len(split_name) > 2:
            hints.append("They have a middle name")
        if "." in author_name:
            hints.append("The name is initialized")
        if len(split_name) == 2 and "." not in author_name:
            hints.append("No middle name and the name is not initialized")
        hints.append(f"The last name length is {len(split_name[-1])}")
        hints.append(f"The first name length is {len(split_name[0])}")

        return hints

    def game_loop(self):
        """Run the main loop. Give a quote and ask for 4 guesses. After each game, ask for new game."""
        new_game = "y"
        while new_game.lower() == "y":
            quote = choice(self.quotes)
            hints = self.generate_hints(quote["author"])

            print(f"Quote: {quote['quote']}")
            user_input = ""
            guess_no = 4

            while user_input.lower() != quote["author"].lower():
                if guess_no == 0:
                    print(f"No more guesses! It was {quote['author']}!")
                    break

                user_input = input(f"Who said it? Guesses remaining {guess_no}\n")
                if user_input.lower() == quote["author"].lower():
                    print(f"Great! You guessed the author in {5 - guess_no} attempts!")
                elif guess_no == 4:
                    guess_no -= 1
                    print(f"Hint: {quote['author_born']}")
                else:
                    guess_no -= 1
                    print(f"Hint: {hints.pop(randint(0, len(hints) - 1))}")
            new_game = input("Do you want to play again (y/n)? ")


if __name__ == "__main__":
    # Generate the CSV, can have logic here to just use CSV
    # qs = QuoteScraper()
    # qs.scrape_site()
    # # print(qs.quotes)
    # qs.make_csv()

    # Read from CSV and run the game
    qg = QuoteGame()
    qg.get_quotes()
    qg.game_loop()
