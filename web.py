import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import pandas as pd

# Task 1: Print the number
number = 305445
print(f"Number: {number}")

# Task 2: Display the image
img_url = "https://sajhajobs.com/storage/jobs/images/RmlcKBmsC4dLlQ9jtglxhiFEDAGCjs83Dr2QKVxM.jpg"
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
img.show()

# Task 3: Scrape the website content
website_url = "https://sajhajobs.com/"
response = requests.get(website_url)
soup = BeautifulSoup(response.content, "html.parser")

# Removing script and style elements
for script_or_style in soup(["script", "style"]):
    script_or_style.decompose()

# Get text and remove extra whitespace
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

# Formatting the content for saving
formatted_content = {
    "Website URL": [website_url],
    "Scraped Content": [text]
}

# Creating a DataFrame
df = pd.DataFrame(formatted_content)

# Saving to an Excel file
excel_file_path = "scraped_content.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Scraped content saved to {excel_file_path}")
