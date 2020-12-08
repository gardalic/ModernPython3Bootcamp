import requests
from bs4 import BeautifulSoup

# response = requests.get("http://quotes.toscrape.com/page/11/")
# print(response)
response = requests.get("http://quotes.toscrape.com/page/10/").text

# print(response)
soup = BeautifulSoup(response, "html.parser")
quotes = soup.findAll("div", {"class": "quote"})
# if quotes: print(True)
# print(quotes[0].find("span", {"class": "text"}).get_text())
# print(quotes[0].find("small", {"class": "author"}).get_text())
# link = quotes[0].find("a")["href"]
print(quotes[0].find("a")["href"])
