import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")

    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)

    return all_books


def get_title(book):
    # Find h3 tag, within it the anchor tag, and get the title attribute
    return book.find("h3").find("a")["title"]


def get_price(book):
    # If we use select we can use CSS syntax and select the class
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    # Get the class name from star-rating main class
    rating = book.select(".star-rating")[0].get_attribute_list("class")[-1]
    return int(ratings[rating])


def db_connection(db_path):
    """Creates a connection, creates the books table if it doesn't exist, and
    returns the connection."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        sql = "CREATE TABLE books (title TEXT, price DOUBLE, rating INTEGER)"
        c.execute(sql)
    except sqlite3.OperationalError:
        print("Table 'books' exists, skipping creation...")
    return conn


def insert_books(book, cursor):
    """Check if input is list or a single tuple, insert everything into the DB."""
    insert_sql = "INSERT INTO books VALUES (?,?,?)"
    if isinstance(book, list):
        cursor.executemany(insert_sql, book)
    elif isinstance(book, tuple):
        cursor.execute(insert_sql, book)
    else:
        print("Did not recieve list or tuple, skipping insert...")


url = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
db_path = "book_scraping_project/books.db"

all_books = scrape_books(url)
conn = db_connection(db_path)
cur = conn.cursor()

# insert_books(all_books, cur)
sql = "SELECT * FROM books"
res_list = cur.execute(sql).fetchall()

for item in res_list:
    print(item)

conn.commit()
conn.close()
