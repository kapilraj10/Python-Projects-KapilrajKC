import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of the page to scrape
url = 'https://sajhajobs.com/job-details/27431'
driver.get(url)

# Give the page some time to load
time.sleep(5)

# Get the page source after JavaScript has rendered
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Close the WebDriver
driver.quit()

# Initialize an empty list to store the product data
products = []

# Assuming the structure of your HTML is similar to the example provided
# Find the relevant elements
image_tag = soup.find('img', {'alt': 'Article Image of job Vacancy Announcement For 469 Candidates To Work In UAE'})
lt_number_tag = soup.find('h4', {'class': 'hiring-name'})

# Extract the necessary data
image_src = image_tag['src'] if image_tag else 'No image'
lt_number = lt_number_tag.find('span', {'class': 'name'}).text.strip() if lt_number_tag else 'No LT number'

# Store the data in the list
products.append([image_src, lt_number])

# Convert the list to a DataFrame
df = pd.DataFrame(products, columns=['Image Source', 'LT Number'])

# Write the DataFrame to an Excel file
excel_file = 'products.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data has been written to {excel_file}")