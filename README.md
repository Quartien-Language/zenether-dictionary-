# 🌌 Zenether Dictionary API

This is the backend for the Zenether language dictionary. Built using FastAPI, it supports endpoints to search, browse, and retrieve information about words in the Zenether conlang.

## 🚀 Features

- `/words/` — List all dictionary entries
- `/words/search?q=` — Search by English or Zenether
- `/words/{id}/` — Lookup word by ID
- `/themes/` — List all semantic themes

## 🛠 How to Run on Replit

1. Create a new Replit using this code.
2. Ensure `requirements.txt` is present.
3. Click the green "Run" button.
4. Visit `/docs` to see the API docs.

## 📁 Data Structure

Each word includes:
- `english` — English word
- `zenether` — Zenether translation
- `pos` — Part of speech
- `pronunciation` — IPA or phonetic
- `notes` — Meaning, poetic value, etc.
- `theme` — Semantic category
- `frequency` — Use frequency or priority

You can expand the dictionary in `main.py` or load from a file/database later.

---
