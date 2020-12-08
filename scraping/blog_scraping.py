# https://www.rithmschool.com/blog

import requests
import csv
from bs4 import BeautifulSoup

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")  # that is the tag used on the blog

with open("scraping/blog_data.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")  # for the "a" tag which has the title and link
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]

        csv_writer.writerow([title, url, date])
        # print(f"{title}: @ {url} - {date}")
