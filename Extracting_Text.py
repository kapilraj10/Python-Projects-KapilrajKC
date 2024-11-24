import requests as r 
from bs4 import BeautifulSoup

resp =r.get("https://kapilrajkc.com.np")
soup =BeautifulSoup(resp.content, "html.parser")

soup.a
print(soup.a)
soup.a.get_text()
print(soup.a.text)
soup.a.string
print(soup.ul)
soup.ul.get_text()
print(soup.ul.get_text())
soup.ul.text
print(soup.ul.text)
soup.ul.string
#print(soup.ul.string)
#print(soup.a.get_text, "of type", type(soup.a.get_text))
#print(soup.a.string, "of type", type(soup.a.string))

#soup.ul.text
#soup.ul.get_text()
#soup.ul.get_text(separator=",",strip=True)