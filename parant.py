import requests as r
from bs4 import BeautifulSoup
from bs4 import NavigableString

# Fetch the webpage
resp = r.get("https://kapilrajkc.com.np")
soup = BeautifulSoup(resp.content, "html.parser")

# Access and prettify the first <ul> element
print(soup.ul.prettify())

# Filter out NavigableString objects from children
def no_nav_string(iterable):
    return list(filter(lambda x: type(x) != NavigableString, iterable))

children = no_nav_string(soup.ul.children)
print("Children:", children)

# Filter out NavigableString objects from descendants
descendants = no_nav_string(soup.ul.descendants)
print("Descendants:", descendants)

if descendants:
    # Access the first descendant and its parent
    first_desc = descendants[0]
    print("First Descendant:", first_desc)
    print("Parent of First Descendant:", first_desc.parent)
else:
    print("No descendants found.")
