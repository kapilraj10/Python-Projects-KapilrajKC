import requests

url = "https://kapilrajkc.com.np"

# Send a GET request to the URL
response = requests.get(url)

# Print the response object
print(response)

# Print the type of the response object
print(type(response))

# Print the response headers
print(response.headers)

# Print the 'Content-Type' header
print(response.headers.get('Content-Type'))

# Use a User-Agent header to simulate a browser request
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Print the response object after adding User-Agent header
print(response)

# Attempt to parse JSON content (if applicable)
try:
    print(response.json())
except ValueError:
    print("Response is not in JSON format")

# Print the request headers sent
print(response.request.headers)
