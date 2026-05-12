# SmartScribe Analytics Engine

An AI-powered content intelligence platform that analyzes, improves, and restructures unstructured text into clean, professional documentation with DITA-style XML output.

---

# Features

- Content analysis with readability scoring and complexity metrics
- AI-powered content rewriting using Groq Llama 3.3 70B
- Persona-based content targeting for Engineer, End Customer, and Sales audiences
- Structure generation with title, summary, steps, and notes extraction
- DITA-style XML output supporting task, concept, and reference topic types
- Content insight engine with quality scoring and improvement suggestions
- 3-stage workflow simulation — Draft, Review, Publish
- Downloadable XML output

---

# Tech Stack

- Python
- Streamlit
- Groq API (Llama 3.3 70B)
- Textstat
- Python-dotenv

---

# Project Structure

```bash
smartscribe-analytics-engine/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── modules/
│   ├── analyzer.py
│   ├── improver.py
│   ├── structure.py
│   ├── xml_generator.py
│   └── insights.py
│
├── utils/
│   └── helpers.py
│
└── assets/
    └── style.css
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartScribe-Analytics-Engine.git
cd SmartScribe-Analytics-Engine
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Rename `.env.example` to `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key from:

https://console.groq.com

---

## 5. Run the Application

```bash
streamlit run app.py
```

After starting the application, open the local Streamlit URL shown in your terminal.

---

# Contributing

Contributions are welcome.

## Contribution Steps

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feat/your-feature-name
```

3. Commit your changes

```bash
git commit -m "feat: add your feature description"
```

4. Push your branch

```bash
git push origin feat/your-feature-name
```

5. Open a Pull Request

---

# Commit Message Convention

| Prefix | Purpose |
|--------|---------|
| feat: | New feature |
| fix: | Bug fix |
| docs: | Documentation changes |
| refactor: | Code restructuring |
| style: | Formatting or UI updates |
| test: | Test-related changes |
| chore: | Maintenance or configuration updates |

---

# Environment Variables

| Variable | Description |
|----------|-------------|
| GROQ_API_KEY | Your Groq API key from console.groq.com |

---

# Upcoming Future Enhancements

- Multi-language documentation support
- PDF and DOCX export
- RAG-based enterprise knowledge integration
- Version-controlled XML publishing
- Team collaboration workflow
- AI-assisted semantic search

---
