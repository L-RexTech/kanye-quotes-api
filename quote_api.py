from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_random_quote():
    try:
        response = requests.get("https://api.kanye.rest/")
        
        if response.status_code == 200:
            quote_data = response.json()
            return {
                "quote": quote_data["quote"],
                "author": "Kanye West",
                "success": True
            }
        else:
            return {
                "error": "Failed to fetch quote",
                "success": False
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "error": f"Unable to connect to the quotes API - {str(e)}",
            "success": False
        }

@app.route('/')
def home():
    return jsonify({
        "message": "Quote API is running!",
        "endpoints": {
            "/": "This help message",
            "/quote": "Get a random quote"
        }
    })

@app.route('/quote')
def quote():
    result = get_random_quote()
    return jsonify(result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print("Starting Quote API server...")
    print(f"Visit http://localhost:{port} for help")
    print(f"Visit http://localhost:{port}/quote for random quotes")
    app.run(host='0.0.0.0', port=port, debug=False)
