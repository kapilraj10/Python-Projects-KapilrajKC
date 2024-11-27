import requests
from bs4 import BeautifulSoup
web = requests.get("https://www.kapilrajkc.com.np/")
#print(web)
soup =BeautifulSoup(web.content,"html.parser")
#lines = soup.find_all("p")
#print(lines)
#for l in lines:
    #print(l.text)
#s = soup.find("div",class_="home-hero__info")
#print(s)
#lines = s.find_all("p")
#print(lines)
#for l in lines:
    #print(l.text)
    