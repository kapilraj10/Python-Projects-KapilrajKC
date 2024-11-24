import requests as r
from bs4 import BeautifulSoup

# Fetch the webpage content
resp = r.get("https://kapilrajkc.com.np")
soup = BeautifulSoup(resp.content, "html.parser")

# Access the first <ul> tag
first_ul = soup.ul
print("First <ul>:", first_ul)

# Access the first <li> within the first <ul>
first_li = soup.ul.li
print("First <li> in <ul>:", first_li)

# Access the second <li> by using next_sibling
second_li = first_li.next_sibling.next_sibling
print("Second <li> in <ul>:", second_li)

# Navigate back to the first <li> by using previous_sibling
back_to_first_li = second_li.previous_sibling.previous_sibling
print("Back to first <li>:", back_to_first_li)
