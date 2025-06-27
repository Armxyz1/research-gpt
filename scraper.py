import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text() for p in paragraphs[:5])
    except:
        return ""
