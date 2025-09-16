import requests
import json

def get_random_quote():
    try:
        response = requests.get("https://api.kanye.rest/")
        
        if response.status_code == 200:
            quote_data = response.json()
            quote = quote_data["quote"]
            return f'"{quote}" - Kanye West'
        else:
            return "Failed to fetch quote"
            
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to the quotes API - {e}"

if __name__ == "__main__":
    print("Random Quote of the Day:")
    print("=" * 40)
    print(get_random_quote())
