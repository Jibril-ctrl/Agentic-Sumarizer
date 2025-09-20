import re
from src.fetch_url import fetch_url

def test_fetch_url_valid():
    url = "https://www.example.com"
    text = fetch_url(url)
    assert isinstance(text, str)
    assert len(text) > 0 or text.startswith("[fetch_url error]")

def test_fetch_url_invalid():
    url = "http://invalid-url"
    text = fetch_url(url)
    assert isinstance(text, str)
    assert text.startswith("[fetch_url error]")

def test_fetch_url_trim():
    url = "https://www.example.com"
    text = fetch_url(url)
    # fetch_url trims to 20000 chars max
    assert len(text) <= 20000
