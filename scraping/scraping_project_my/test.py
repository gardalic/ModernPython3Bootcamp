import requests
from bs4 import BeautifulSoup

# response = requests.get("http://quotes.toscrape.com/page/11/")
# print(response)
response = requests.get('http://quotes.toscrape.com/author/J-M-Barrie')

# print(response.content)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find(class_="author-description")
print(quotes)
# print(quotes)