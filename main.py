
from fastapi import FastAPI
from services import get_trends

BRAZIL_WOE_ID = 23424768

app = FastAPI()


@app.get("/")
async def root():
    trends = get_trends(23424768)
    return trends


