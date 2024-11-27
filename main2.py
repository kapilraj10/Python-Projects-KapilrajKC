import requests
from bs4 import BeautifulSoup
web = requests.get("https://www.kapilrajkc.com.np/")
soup = BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
for i in soup.find_all("a"):
    print(i.get("href"))
    
