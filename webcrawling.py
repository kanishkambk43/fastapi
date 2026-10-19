from fastapi import FastAPI
import httpx
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/scrape")
def scrape(url: str):

    response = httpx.get(url) #output-->>><Response [200 OK]>

    soup = BeautifulSoup(response.text, "html.parser")#response.text->>actual HTML content

    title = soup.title.text

    return {
        "url": url,
        "title": title
    }