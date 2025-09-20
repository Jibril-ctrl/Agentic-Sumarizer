# 📘 Agentic Summarizer

**Author:** Jibril Anifowoshe  
**Date:** September 2025  
**License:** MIT (with attribution required — see LICENSE and TRADEMARKS)  

---

## 🚀 Overview

The **Agentic Summarizer** is a local, agent-style research assistant that:

- Fetches and cleans articles from the web.  
- Summarizes them into **EXACTLY 5 executive-style bullet points.**  
- Supports **single-URL summaries** *or* **multi-URL (3) summaries + comparison.**  
- Saves outputs to `.md` and optional `.pdf` files, branded with a signature footer.  

It runs **fully offline** using [Ollama](https://ollama.com/) and the free **Llama 3.2 3B** model.  
LangChain’s `@tool` decorator is used minimally to keep tools (`fetch_url`, `save_note`) cleanly callable.  

---

## ✨ Features

- 📝 **Summarize any article** into 5 numbered bullets.  
- 📊 **Compare 3 articles** (common themes, differences, standout insights, takeaway).  
- 💾 **Save results** to Markdown + PDF with attribution footer.  
- 🔒 **Offline, private, and free** — runs entirely on your machine via Ollama.  
- ⚡ **Fast-mode trims** (single URL 2800 chars, batch 2000 chars each).  
- 📂 **Organized repo structure** with `src/`, `examples/`, and notebook.  

---

## 🛠️ Requirements

- **Python 3.9+**  
- **Ollama** (installed + running)  
- Models:  
  ```bash
  ollama serve
  ollama pull llama3.2:3b
  ```

Python dependencies (see `requirements.txt`):
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1) Start Ollama
```bash
ollama serve
```

2) Pull the model
```bash
ollama pull llama3.2:3b
```

3) Launch Jupyter and open the notebook
```bash
jupyter notebook
```

Run the notebook cells in order. Use the **Single URL** tab for one page, or **3 URLs + Compare** for multi-source analysis.

---

## 🧠 Architecture & Design

- **LangChain `@tool`** → only for clean `.invoke()` calls of `fetch_url` and `save_note`.  
- **Direct Ollama API** → faster and simpler for summarization and comparison prompts.  
- **Stop tokens** → ensure **exactly 5 bullets** by halting at `\n6.` etc.  
- **Trim input** → 2,800 chars (single) / 2,000 chars (batch) balance speed and context.  
- **ReportLab** → optional PDF export for executive-ready outputs.  

### “Perfect World” Notes
With paid APIs (OpenAI/Claude) you could:  
- Use larger-context models and richer analyses.  
- Add autonomous agent routing (LangChain agents).  
- Store and search summaries in a vector DB.  
- Ship a slick web app (Streamlit/Gradio).  

---

## 📂 Project Structure

```
agentic-summarizer/
│
├── notebooks/
│   └── agentic_summarizer.ipynb
│
├── src/
│   ├── fetcher.py
│   ├── saver.py
│   ├── summarizer.py
│   └── utils.py
│
├── tests/
│   └── test_utils.py
│
├── examples/
│   ├── test_single.md
│   └── test_batch.md
│
├── docs/
│   └── Agentic_Summarizer_Walkthrough_*.docx
│
├── LICENSE.md
├── TRADEMARKS.md
├── requirements.txt
└── README.md
```

---

## 🧪 Tests

Run basic tests for helpers:
```bash
pip install pytest
pytest -q
```

---

## ⚖️ License & Attribution

Licensed under the **MIT License** (see `LICENSE.md`).  

> **Trademark Notice:**  
> *Agentic Summarizer™ is a prototype project authored by **Jibril Anifowoshe**.  
> Any use of the name, branding, or signature footer must include proper attribution.*
