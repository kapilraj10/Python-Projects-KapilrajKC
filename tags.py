import requests as r
from bs4 import BeautifulSoup
resp =r.get("https://kapilrajkc.com.np")
soup = BeautifulSoup(resp.content, "html.parser")
soup.title
soup.h1
print(soup.h1)
soup.div
first_div = soup.div
type(first_div)
first_div.attrs
first_div.div.div.attrs
first_div.attrs['class'].append("some-other-class")
first_div
soup.div
