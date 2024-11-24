import requests as r
from bs4 import BeautifulSoup

def get_price_information(ticker, exchange):
    # Correctly format the URL for Google Finance
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    
    # Make the request
    resp = r.get(url)
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(resp.content, "html.parser")
    
    # Find the element containing the price data
    price_div = soup.find("div", attrs={"class": "YMlKec fxKbKc"})
    
    # Check if the price_div was found
    if price_div:
        # Extract the price as a string and remove the currency symbol
        price_text = price_div.text.strip().replace(",", "")
        price = float(price_text[1:])  # Skipping the first character (currency symbol)
        
        # Here you should map or infer the currency based on exchange
        # For now, assume USD unless known otherwise
        currency = price_text[0]  # Using the first character as a proxy for currency symbol
        
        # Return the information as a dictionary
        return {
            "ticker": ticker,
            "exchange": exchange,
            "price": price,
            "currency": currency,
        }
    else:
        return {"error": "Price information not found"}

if __name__ == "__main__":
    print(get_price_information("MSFT", "NASDAQ"))
