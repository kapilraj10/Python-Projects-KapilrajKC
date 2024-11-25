import requests
from bs4 import BeautifulSoup
web = requests.get("https://sajhajobs.com")
soup = BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
img = soup.find_all("img")
print(img)
for i in img:
   print(i)
for i in img:
   print(i.get("src"))
   print(type(i.get("src")))
   for i in img:
      print(i.get("alt"))
      