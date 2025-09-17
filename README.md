# Kanye West Quotes API 🎤

A simple Python Flask API that serves random Kanye West quotes. Perfect for adding some Kanye wisdom to your projects!

## Features

- 🚀 **Fast API** built with Flask
- 🔥 **Random Kanye quotes** from the kanye.rest API
- 🌐 **Easy deployment** to Railway, Render, or Heroku
- 📱 **Mobile friendly** JSON responses
- 🆓 **Completely free** to use and deploy

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and available endpoints |
| `/quote` | GET | Get a random Kanye West quote |

## Example Responses

### GET /
```json
{
  "message": "Quote API is running!",
  "endpoints": {
    "/": "This help message",
    "/quote": "Get a random quote"
  }
}
```

### GET /quote
```json
{
  "quote": "I feel like I'm too busy writing history to read it.",
  "author": "Kanye West",
  "success": true
}
```

## Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/kanye-quotes-api.git
cd kanye-quotes-api
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the API**
```bash
python quote_api.py
```

4. **Test the API**
```bash
curl http://localhost:5000/quote
```

### Using the Simple Script

Run the standalone quote generator:
```bash
python quote_generator.py
```

## Deployment

### Railway (Recommended)
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Railway auto-detects Flask and deploys!

### Render
1. Go to [render.com](https://render.com)
2. Create "Web Service"
3. Connect your GitHub repo
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python quote_api.py`

### Heroku
```bash
heroku create your-app-name
git push heroku main
```

## Files Structure

```
kanye-quotes-api/
├── quote_api.py          # Main Flask API
├── quote_generator.py    # Simple CLI script
├── requirements.txt      # Python dependencies
├── Procfile             # For Heroku deployment
├── README.md            # This file
└── deploy_instructions.md # Detailed deployment guide
```

## Dependencies

- **Flask** - Web framework
- **Requests** - HTTP library for API calls
- **Gunicorn** - WSGI server for production

## Usage Examples

### JavaScript/Node.js
```javascript
fetch('https://your-api-url.railway.app/quote')
  .then(response => response.json())
  .then(data => console.log(data.quote));
```

### Python
```python
import requests
response = requests.get('https://your-api-url.railway.app/quote')
quote_data = response.json()
print(quote_data['quote'])
```

### cURL
```bash
curl https://your-api-url.railway.app/quote
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- Quotes provided by [kanye.rest](https://kanye.rest) API
- Built with ❤️ and Python

---

**"I am a god"** - Kanye West (and this API proves it! 🔥)
