import re
import requests
from bs4 import BeautifulSoup
from readability import Document

def fetch_url(url: str) -> str:
    """Fetch a page and return cleaned article text."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(url, headers=headers, timeout=20).text
        article_html = Document(html).summary(html_partial=True)
        text = BeautifulSoup(article_html, "html.parser").get_text("\n")
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return text[:20000]
    except Exception as e:
        return f"[fetch_url error] {e}"
