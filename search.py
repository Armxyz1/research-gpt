import wikipedia
import requests
from bs4 import BeautifulSoup

def search_wikipedia(query):
    """Returns a short summary from Wikipedia or None if not found."""
    try:
        return wikipedia.summary(query, sentences=5)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation: {', '.join(e.options[:5])}"
    except:
        return None

def search_arxiv(query, max_results=3):
    """Searches arXiv and returns a list of abstracts."""
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    try:
        response = requests.get(url)
        entries = response.text.split("<entry>")[1:]
        abstracts = []
        for entry in entries:
            start = entry.find("<summary>") + 9
            end = entry.find("</summary>")
            if start > 8 and end != -1:
                abstract = entry[start:end].strip()
                abstracts.append(abstract)
        return abstracts
    except Exception as e:
        print(f"[arXiv error] {e}")
        return []

def search_duckduckgo(query, max_results=3):
    """Scrapes DuckDuckGo HTML results and returns URLs."""
    url = "https://html.duckduckgo.com/html/"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.post(url, data={"q": query}, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for a in soup.find_all("a", class_="result__a", href=True):
            links.append(a["href"])
            if len(links) >= max_results:
                break
        return links
    except Exception as e:
        print(f"[DuckDuckGo error] {e}")
        return []
