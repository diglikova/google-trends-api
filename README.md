# Google Trends API with FastAPI

This is a minimal FastAPI application that uses pytrends to detect suspicious spikes in search interest over the past 7 days.

## Endpoints

- `/`: Health check
- `/trend?keyword=bitcoin`: Get search trend data for a keyword

## Deploy

Use on [Render](https://render.com) with:

- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host=0.0.0.0 --port=10000`
