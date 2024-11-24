import requests as r

# Define the API Key and URL
API_KEY = "YOUR_API_KEY_HERE"
url = "https://testapi.io/api/Kapilrajkc10/https://testapi.io/api/Kapilrajkc10/"

# Define headers for the request with proper formatting
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Send a GET request with headers
response = r.get(url, headers=headers)

# Print the response status and content
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# Basic Auth example
auth = ("user1", "pass2")
response_auth = r.get(url, auth=auth)

# Print the basic auth response status and content
print("Basic Auth Status Code:", response_auth.status_code)
if response_auth.status_code == 200:
    print("Basic Auth Response JSON:", response_auth.json())
else:
    print(f"Failed to retrieve data with basic auth. Status code: {response_auth.status_code}")

# Import statement for handling responses (assuming you need it for other purposes)
# 'responces' should be 'responses', but this import is not typically needed
# Remove the import if it's not necessary
# import responses
