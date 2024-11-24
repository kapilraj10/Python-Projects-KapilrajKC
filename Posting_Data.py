import requests as r

# URLs to fetch data from
urls = {
    "Qatar": "https://www.baideshikrojgar.site/search/label/Qatar",
    "Cyprus": "https://www.baideshikrojgar.site/search/label/Cyprus",
    "UAE": "https://www.baideshikrojgar.site/search/label/UAE",
    "News": "https://www.baideshikrojgar.site/search/label/News"
}

# Fetch and print data from each URL
for key, url in urls.items():
    response = r.get(url)
    try:
        # Attempt to parse JSON data
        data = response.json()
        print(f"{key} Data:")
        print(data)
    except ValueError:
        print(f"{key} URL did not return JSON data.")
        print(response.text)  # Print the raw HTML if not JSON

# POST requests
post_urls = [
    {"url": "https://www.baideshikrojgar.site/search/label/News", "data": {"key1": "Value1"}},
    {"url": "https://www.baideshikrojgar.site/search/label/News", "data": {"key1": "Value1", "key2": "a value with spaces and an apostrophe"}},
    {"url": "https://www.baideshikrojgar.site/search/label/News", "data": "some text"}
]

for post in post_urls:
    response = r.post(post["url"], data=post["data"])
    print(f"POST to {post['url']}:")
    print("Status Code:", response.status_code)
    print("Request Body:", response.request.body)
    try:
        # Attempt to parse JSON data
        data = response.json()
        print("Response JSON Data:")
        print(data)
    except ValueError:
        print("Response did not return JSON data.")
        print(response.text)  # Print the raw HTML if not JSON
