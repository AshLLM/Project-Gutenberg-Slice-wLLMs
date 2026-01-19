# Slicing Text with LLMs

This is a small Python / Jupyter project where I experiment with slicing and processing text using an LLM (OpenAI API) and some basic NLP tools from NLTK. The notebook is mainly meant as a learning project and a reference for future experiments.

---

## Project Files

```text
.
├── slicing_text_llm.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. (Optional but recommended) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK data

This project uses NLTK tokenization, which requires downloading some extra data once:

```python
import nltk
nltk.download("punkt")
```

---

## OpenAI API Key

The notebook uses the OpenAI API. The API key is **not** included in the code.

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your_api_key_here
```

The notebook loads this using `python-dotenv`. The `.env` file is ignored by Git and should not be committed.

---

## Running the Notebook

After setup, start Jupyter:

```bash
jupyter notebook
```

Open `slicing_text_llm.ipynb` and run the cells in order.

---

## Notes

* This is a learning project, not a production-ready application.
* Running the notebook will make API calls that may cost money depending on your OpenAI plan.
* Make sure your API key stays private.

---

## License

No license has been added yet. Feel free to use this code for learning or personal projects.

