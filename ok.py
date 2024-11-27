import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch and parse a single page
def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Initialize lists to store data
lt_numbers = []
img_sources = []

# Base URL and initial page
base_url = 'https://sajhajobs.com/job-listing?c=18'

# Function to extract LT Numbers and Images from a page
def extract_data_from_page(soup):
    # Extract LT Numbers
    for h4 in soup.find_all('h4', class_='hiring-name'):
        if 'LT Number' in h4.text:
            lt_number = h4.find('span', class_='name').text.strip()
            lt_numbers.append(lt_number)

    # Extract Image Sources
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            img_sources.append(src)

# Fetch the first page and start scraping
page_number = 1
while True:
    url = f'{base_url}&page={page_number}'
    print(f'Scraping page {page_number}...')
    
    soup = fetch_page(url)
    
    # Extract data from the current page
    extract_data_from_page(soup)
    
    # Check if there's a next page
    next_page = soup.find('a', class_='next')
    if next_page:
        page_number += 1
    else:
        break

# Create a DataFrame
df = pd.DataFrame({
    'LT Number': lt_numbers,
    'Image Source': img_sources[:len(lt_numbers)]  # Adjust length if needed
})

# Save to Excel
df.to_excel('job_details.xlsx', index=False)

print("Data has been scraped and saved to 'job_details.xlsx'")
