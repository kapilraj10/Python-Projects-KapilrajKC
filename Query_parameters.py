import requests as r

# Define the URL
url = "https://testapi.io/api/Kapilrajkc10/https://testapi.io/api/Kapilrajkc10/"

# Send a GET request to the URL
resp = r.get(url)

# Print the response object
print("Response:", resp)

# Check if the request was successful
if resp.status_code == 200:
    # Parse JSON response
    data = resp.json()
    print("Exchange Rate for USD:", data['data']['rates']['USD'])
else:
    print(f"Failed to retrieve data. Status code: {resp.status_code}")

# Example with parameters (Note: The Coinbase API does not use these parameters)
params = { "currency": "BTC" }
resp = r.get(url, params=params)

# Print the data again
if resp.status_code == 200:
    data = resp.json()
    print("Exchange Rate for USD (with params):", data['data']['rates']['USD'])
else:
    print(f"Failed to retrieve data. Status code: {resp.status_code}")

# Example with headers (Note: This API does not require these headers)
headers = {
    "User-Agent": "Mozilla/5.0"
}
resp = r.get(url, headers=headers)

# Print status code and JSON response
print("Status Code:", resp.status_code)
if resp.status_code == 200:
    data = resp.json()
    print("Exchange Rate for USD (with headers):", data['data']['rates']['USD'])
else:
    print(f"Failed to retrieve data. Status code: {resp.status_code}")

# Print request URL and headers
print("Request URL:", resp.request.url)
print("Request Headers:", resp.request.headers)
