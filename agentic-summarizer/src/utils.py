import re
from urllib.parse import urlparse
from datetime import datetime

def smart_filename_from_url(url: str, fallback: str = "summary") -> str:
    try:
        host = urlparse(url).netloc or ""
        host = re.sub(r"^www\.", "", host)
        host = re.sub(r"[^a-zA-Z0-9_-]+", "_", host).strip("_")
        date = datetime.now().date().isoformat()
        return f"{host or fallback}_{date}"
    except Exception:
        return fallback

def normalize_basename(name: str) -> str:
    name = (name or "").strip().lstrip(". ").strip()
    for ext in (".md", ".pdf", ".txt", ".markdown"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    return name

def format_numbered_five(raw: str, url: str) -> str:
    title = f"### Here’s the summary of {url}\n"
    text = (raw or "").strip()
    pts = re.split(r"(?m)^\s*(\d{1,2})\.\s+", text)
    numbered = []
    if len(pts) > 1:
        for i in range(1, len(pts) - 1, 2):
            body = pts[i+1].strip()
            if body:
                numbered.append(body)
        numbered = numbered[:5]
    if not numbered:
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        cleaned = []
        for ln in lines:
            ln = re.sub(r"^\s*[-•\d]+\s*[.)-]?\s*", "", ln)
            if ln:
                cleaned.append(ln)
        numbered = cleaned[:5]
    while len(numbered) < 5:
        numbered.append("…")
    bullets = "\n".join(f"{i}. {p}" for i, p in enumerate(numbered, 1))
    return f"{title}\n{bullets}"
