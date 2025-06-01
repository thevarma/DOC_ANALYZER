# 📘 DOC_ANALYZER – AI-Powered Documentation Improvement Agent

## 📌 Objective

This project is an AI-powered documentation analyzer developed for the MoEngage Tech Internship assignment.  
It evaluates and improves help documentation using the following criteria:

- **Readability for marketers**
- **Structure and logical flow**
- **Completeness of information and examples**
- **Adherence to writing style guidelines (e.g., Microsoft Style Guide)**

Includes a bonus reviser module that automatically rewrites content for better clarity, tone, and accessibility.

---

## ⚙️ Architecture

```plaintext
Input URL 
   ↓
Scraper (Playwright) 
   ↓
Cleaned HTML 
   ↓
Analyzer (LangChain + Gemini) 
   ↓
JSON Report (Suggestions)
   ↓
[Optional] Reviser (Gemini) 
   ↓
Final Improved Markdown
```

---

## 🧩 Modules Overview

### 1. `scraper/` – Web Scraper
- Built with **Playwright** for scraping JavaScript-heavy pages.
- Wait strategies ensure dynamic content is fully loaded.
- Uses **BeautifulSoup** for HTML parsing.

### 2. `analyzer/` – Document Evaluator
- Utilizes **LangChain** + **Google Gemini API** for LLM-based evaluations.
- Measures **readability** using Flesch-Kincaid.
- Outputs suggestions categorized by: Readability, Structure, Completeness, and Style.

### 3. `reviser/` – Bonus AI Rewriter
- Applies selected improvements to rewrite documentation.
- Uses **Gemini API** to revise text with better tone, clarity, and structure.

### 4. `utils/` – Helper Functions
- HTML cleanup
- Prompt formatting
- Scoring and validation utilities

---

## 📈 Key Features

- ✅ JavaScript-aware scraping with **Playwright**
- ✅ LLM-based readability & style evaluation
- ✅ JSON output with structured suggestions
- ✅ Auto-rewriting of documentation (bonus)
- ✅ Modular Python architecture for easy integration

---

## 🧪 Output Format

- `sample_report.json`: Includes detailed suggestions categorized by criteria
- `revised_article.md`: Revised version of input article using Gemini
- `screenshots/`: Shows tool in action

---

## 🚀 How to Run

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set your API key**
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

3. **Run analyzer**
```bash
python main.py https://help.moengage.com/hc/en-us/articles/sample-url
```

4. **Run reviser (optional)**
```bash
python reviser.py outputs/sample_report.json
```

---

## 🛠️ Technologies Used

- Python
- Playwright
- LangChain
- Google Gemini API
- BeautifulSoup
- dotenv
- tqdm

---

## 🧠 Assumptions & Design Choices

- Pages load content via JavaScript → used Playwright over HTTP libraries.
- LLM prompting structured to maintain JSON format → reduced output parsing errors.
- Tailored readability analysis to **marketer persona** with specific scoring logic.

---

## 📚 License

This project is intended for educational and internship evaluation purposes only.
