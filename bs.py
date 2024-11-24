import requests as r 
from bs4 import BeautifulSoup

resp = r.get("https://www.kapilrajkc.com.np/")
if resp.status_code == 200:
    print("Content:", resp.content)
    
    soup = BeautifulSoup(resp.content, "html.parser")  # or "lxml"
    print(type(soup))
    
    print(soup)
    print(soup.title)
    print(soup.prettify())
else:
    print(f"Failed to retrieve content. Status code: {resp.status_code}")

print(soup.h4)