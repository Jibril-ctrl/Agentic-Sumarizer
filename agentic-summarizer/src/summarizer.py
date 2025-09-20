import requests

MODEL = "llama3.2:3b"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

SYSTEM = """You are a concise research agent.
Return EXACTLY 5 bullets as a NUMBERED LIST:
1. ...
2. ...
3. ...
4. ...
5. ...
- Executive tone, no preamble or closing lines.
- No quotes, no code fences, no extra bullets.
"""

def _ollama_generate(prompt: str,
                     model: str = MODEL,
                     num_predict: int = 240,
                     num_ctx: int = 2048,
                     timeout_s: int = 35) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "temperature": 0,
            "stop": ["\n6.", "\n## ", "\n### "]
        }
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=timeout_s)
    r.raise_for_status()
    return r.json().get("response", "")

def summarize_text(article_text: str, max_chars: int = 2800) -> str:
    txt = (article_text or "")[:max_chars]
    prompt = f"{SYSTEM}\n\nSummarize into EXACTLY 5 numbered bullets (1–5):\n\n{txt}"
    return _ollama_generate(prompt)

def compare_summaries(a: str, b: str, c: str) -> str:
    prompt = (
        "You are a concise analyst. Compare the three summaries provided.\n"
        "Output exactly this structure:\n"
        "Common themes:\n1. ...\n2. ...\n3. ...\n"
        "Key differences:\n1. ...\n2. ...\n3. ...\n"
        "Standout insight per source:\nA) ...\nB) ...\nC) ...\n"
        "Takeaway:\nOne sentence. Be crisp and non-redundant.\n\n"
        f"Summary A:\n{a}\n\nSummary B:\n{b}\n\nSummary C:\n{c}\n"
    )
    return _ollama_generate(prompt, num_predict=220, num_ctx=2048)
