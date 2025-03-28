from fastapi import FastAPI, Query
from pytrends.request import TrendReq

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/trend")
def get_trend(keyword: str = Query(...)):
    pytrends = TrendReq(hl="en-US", tz=0)
    pytrends.build_payload([keyword], cat=0, timeframe="now 7-d")
    df = pytrends.interest_over_time()

    if df.empty or len(df) < 2:
        return {"trend": keyword, "error": "Not enough data"}

    v1 = int(df[keyword].iloc[-2])
    v2 = int(df[keyword].iloc[-1])
    growth = ((v2 - v1) / (v1 or 1)) * 100

    return {
        "trend": keyword,
        "from": v1,
        "to": v2,
        "growth": round(growth, 1),
        "suspicious": growth > 30
    }
