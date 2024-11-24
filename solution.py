import requests as r 
from bs4 import BeautifulSoup
resp =r.get("https://kapilrajkc.com.np")
soup = BeautifulSoup(resp.content , "html.parser")
len(soup.find.all())
books_tags = soup.find_all("article", attrs ={"class": "product_pod"})
len(books_tags)
def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["tittle"]
    price = book_tag 
    return title
books_tags[0]

