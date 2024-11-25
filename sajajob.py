import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract LT Numbers and Image URLs from a single page
def extract_details_from_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract LT Numbers
    lt_numbers = [h4.find('span', class_='name').text for h4 in soup.find_all('h4', class_='hiring-name') if 'LT Number' in h4.text]
    
    # Extract image source URLs
    img_sources = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
    
    return lt_numbers, img_sources

def scrape_sajhajobs(url):
    """Scrapes LT Numbers and image URLs from the given URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 400:
        print(f"Failed to retrieve the website content. Status code: {response.status_code}")
        return None
    
    html_content = response.content
    return extract_details_from_page(html_content)

def save_to_excel(lt_numbers, img_sources, filename):
    """Saves the extracted details to an Excel file."""
    df = pd.DataFrame({
        'LT Number': lt_numbers,
        'Image Source': img_sources
    })
    df.to_excel(filename, index=False)

if __name__ == '__main__':
    url = 'https://sajhajobs.com/'  # Replace with the actual target URL
    output_file = 'sajhajobs_data.xlsx'

    result = scrape_sajhajobs(url)
    if result:
        lt_numbers, img_sources = result
        save_to_excel(lt_numbers, img_sources, output_file)
        print('Data saved to', output_file)
    else:
        print('No data extracted.')
