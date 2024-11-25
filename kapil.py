import requests
from bs4 import BeautifulSoup

# Replace this with the URL you want to scrape
url = "https://sajhajobs.com/job-details/27429"
# Setp 1: get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
# Setp 2: get  Parse the HTML
soup = BeautifulSoup(htmlContent, "html.parser")
#print(soup.prettify)

# Setp 3:  HTML Tree Traversal
title = soup.title
print(type(title)) # TAG
(type(soup))   # BeautifulSoup
print(type(title.string)) # NavigableString

markup = "<p><!-- this ia a comment --></p>"
soup2 =BeautifulSoup(markup)
print(type(soup2.p.string))

# get the titel of the HTML paage 
titel = soup.title
#Get all the paragraphs from the page
paras = soup.find_all("p")
print(paras)

print(soup.find('p') ) # get first element in the html page 
print(soup.find('p')['class']) # get classes of any element in the html page 


#find all the elemenets with class lead 
print(soup.find_all("p",class_="lead"))

# Get the text from the elements tags/soup
print(soup.find("p").get_text())
print(soup.get_text())

# Get all the anchor from the page
anchor= soup.find_all("a")
all_links = set()
print(anchor)
#Get all the links on the page:
for link  in anchor:
   if (link.get("href") != "#"):
    linkText = "https://sajhajobs.com/job-details/27429" + link.get("href")
    all_links.add(link)
    print(linkText)
     
# Assuming you have your HTML content in a variable called 'html_content'
soup = BeautifulSoup(htmlContent, 'html.parser')

# Find the element with id "navbarSupportedContent"
navbarSupportedContent = soup.find(id="navbarSupportedContent")

#Iterate through the children of the element and print each one
for elem in navbarSupportedContent.contents:
    print(elem)
for item in navbarSupportedContent.string:
   print(item)
