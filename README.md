# ai-gutenberg-cleaner

A Jupyter notebook pipeline that takes a single **Project Gutenberg ebook page URL** and produces:

1. A structured **metadata JSON** (`metadata/<id>.metadata.json`)
2. A clean **core literary text** (`core_txts/<id>_clean.txt`) with Gutenberg boilerplate and editorial matter removed

---

## How it works

```
gutenberg_url  ─────────────────────────────────────────────────────────┐
                                                                         ▼
                              ┌─────────────────────────────────────────────┐
                              │  1 · Metadata                               │
                              │  Scrape ebook page → metadata/<id>.json     │
                              └──────────────────────┬──────────────────────┘
                                                     │ ebook_no
                                                     ▼
                              ┌─────────────────────────────────────────────┐
                              │  2 · Fetch & preliminary cleanup            │
                              │  Download plain text → gutenberg_cleaner    │
                              │  head[:50 000]  /  tail[-50 000:]           │
                              └──────────────────────┬──────────────────────┘
                                                     │
                                                     ▼
                              ┌─────────────────────────────────────────────┐
                              │  3 · Identify boundaries with AI (6 calls)  │
                              │  Map → Select → Extract  ×  start & end     │
                              └──────────────────────┬──────────────────────┘
                                                     │ anchor strings
                                                     ▼
                              ┌─────────────────────────────────────────────┐
                              │  4 · Extract & save                         │
                              │  Slice text_core → core_txts/<id>_clean.txt │
                              └──────────────────────┬──────────────────────┘
                                                     │
                                                     ▼
                              ┌─────────────────────────────────────────────┐
                              │  5 · NLTK demo                              │
                              │  Tokenise, collocations, concordance, plot  │
                              └─────────────────────────────────────────────┘
```

---

## Project files

```
processing_gutenberg/
├── gutenberg_pipeline.ipynb   ← main notebook (single entry point)
├── helper_functions.py        ← metadata scraping + text utilities
├── requirements.txt
├── OPENAI_KEY.env.example
├── metadata/                  ← persisted metadata JSON files
└── core_txts/                 ← extracted core literary texts
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/AshLLM/Project-Gutenberg-Slice-wLLMs.git
cd Project-Gutenberg-Slice-wLLMs
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Copy the example env file and add your key:

```bash
cp OPENAI_KEY.env.example OPENAI_KEY.env
```

Edit `OPENAI_KEY.env`:

```env
OPENAI_API_KEY=sk-...
```

`OPENAI_KEY.env` is git-ignored and should never be committed.

---

## Usage

Open `gutenberg_pipeline.ipynb`, set `gutenberg_url` in cell 2 to any Gutenberg ebook page URL, and run all cells:

```python
gutenberg_url = "https://www.gutenberg.org/ebooks/84"   # Frankenstein
```

---

## Notes

- Running the notebook makes 6 OpenAI API calls per book.
- `helper_functions.py` contains all utilities (metadata scraping, text normalisation, anchor finding) and can be imported from any other notebook.
- This is a learning/portfolio project, not a production system.
