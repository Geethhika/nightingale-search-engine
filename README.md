# Nightingale Search Engine

## Project Overview
The **Nightingale Search Engine** is a local AI-powered information retrieval system designed to extract precise answers from internal company documents such as meeting transcripts, reports, and planning notes.  
It combines **semantic search** (TF-IDF) and a **local LLM reasoning layer** using **Ollama** and the lightweight **phi3** model to ensure efficiency, privacy, and offline operability.

Goal: Enable users to query documents using natural language and receive concise, contextually relevant responses with cited sources.

---

## Installation & Setup

### 1. System Requirements
- Python 3.10+ (64-bit recommended)  
- At least 4 GB RAM  
- 5 GB free disk space  
- Internet connection (for downloading Ollama and models)

### 2. Install Tools
- **Python**: [Download Python](https://www.python.org/downloads/)  
- **Ollama**: [Download Ollama](https://ollama.com/download)  
  ```bash
  ollama pull phi3
  ollama list  # Should show phi3:latest
3. Clone Repository

bash
Copy code
git clone https://github.com/Geethhika/nightingale-search-engine.git
cd nightingale-search-engine
5. Setup Python Environment

6. 
bash
Copy code
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install --upgrade pip
pip install -r requirements.txt
7. Add Data
Place all .docx or .txt files into the data/ directory.

8. Build Index
bash
Copy code
python src/cli.py --build
This generates TF-IDF embeddings for all documents in models/.

Example Queries
Here are some example questions you can ask the engine:

"What are Nightingale’s Q4 priorities?"

"Who approved the Q3 budget?"

"Summarize the action items from the last team meeting."

"Which employees are assigned to the Nightingale project?"

"What features are being prioritized for clinician feedback?"

Tip: Use --topk N to retrieve more chunks or --simple for a basic summarizer.

Usage Instructions
Basic Query
bash
Copy code
python src/cli.py "What are Nightingale's Q4 priorities?"
Advanced Options
Retrieve top 5 chunks instead of default 4:

bash
Copy code
python src/cli.py "Who approved the Q3 budget?" --topk 5
Use simple summarizer without LLM:

bash
Copy code
python src/cli.py "Summarize last meeting decisions" --simple
Notes
Ensure phi3 is installed in Ollama; it fits within 4 GB RAM.

Place all documents in data/ before building the index.

If you add new documents, run --build again to update the index.

Troubleshooting

Issue	- Solution
Memory error	- Ensure phi3 is used in synthesizer.py instead of larger models
Ollama not found - Check installation and PATH; run ollama --version
Missing Python packages	- pip install -r requirements.txt

