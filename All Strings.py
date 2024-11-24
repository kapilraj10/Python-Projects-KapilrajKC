import requests as r
from bs4 import BeautifulSoup
resp =r.get("https://kapilrajkc.com.np")
soup = BeautifulSoup(resp.content , "html.parser")
soup.stripped_strings
print(soup.stripped_strings)
all_strings = list(soup.stripped_strings)
print(all_strings)
if soup.string is not None:
    print(len(soup.string))
    print("First 10 characters of soup.string :" , soup.styring[:10])
else:
    print("soup.string is None, meaning the document has multiple tags or text nodes:")
#len(all_strings)
#print(len(all_strings))
#len(list(soup.string))
#print(len(list(soup.string)))
#list(soup.string)[:10]
#print(list(soup.string)[:10])

