# Deploy Quote API to Internet

## Option 1: Railway (Free & Easy)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Upload your project files
5. Railway will automatically detect Flask and deploy

## Option 2: Render (Free)

1. Go to https://render.com
2. Sign up and connect GitHub
3. Create new "Web Service"
4. Deploy from repository
5. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python quote_api.py`

## Option 3: ngrok (Local tunnel)

1. Download ngrok from https://ngrok.com/download
2. Run your Flask app: `python quote_api.py`
3. In another terminal: `ngrok http 5000`
4. Use the public URL provided by ngrok

## Option 4: Heroku

1. Install Heroku CLI
2. Create Procfile: `web: gunicorn quote_api:app`
3. Deploy with git commands

Your API will be accessible at the provided URL with endpoints:
- `/` - API information
- `/quote` - Get random quote
