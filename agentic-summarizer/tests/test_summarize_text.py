from src.summarizer import summarize_text

def test_summarize_text_returns_five(monkeypatch):
    # Mock the _ollama_generate to avoid real Ollama call
    monkeypatch.setattr("src.summarizer._ollama_generate", lambda *a, **k: "1. A\n2. B\n3. C\n4. D\n5. E")

    text = "Some article text here."
    summary = summarize_text(text, max_chars=1000)

    assert isinstance(summary, str)
    assert summary.count("\n") >= 4  # should have 5 bullets
