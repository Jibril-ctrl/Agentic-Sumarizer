import os
from src.fetch_url import fetch_url
from src.summarizer import summarize_text
from src.save_note import save_note

def test_end_to_end(tmp_path, monkeypatch):
    # Mock fetch_url to avoid real network
    monkeypatch.setattr("src.fetch_url.fetch_url", lambda url: "Some fetched content.")

    # Mock summarizer to avoid real Ollama
    monkeypatch.setattr("src.summarizer._ollama_generate", lambda *a, **k: "1. A\n2. B\n3. C\n4. D\n5. E")

    # Run pipeline
    text = fetch_url("https://example.com")
    summary = summarize_text(text, max_chars=500)
    filename = tmp_path / "demo"
    result = save_note(str(filename), summary)

    expected_path = f"{filename}.md"
    assert os.path.exists(expected_path)
    with open(expected_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "1. A" in content
        assert "— Jibril Anifowoshe" in content
