from PyPDF2 import PdfReader
import docx
import os, re

def extract_text_from_pdf(path):
    text = []
    with open(path, "rb") as f:
        reader = PdfReader(f)
        for p in reader.pages:
            page_text = p.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def chunk_text(text, chunk_size=200, overlap=40):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def load_and_chunk_docs(data_dir="data"):
    all_chunks = []
    metadata = []

    for fname in os.listdir(data_dir):
        path = os.path.join(data_dir, fname)
        if not os.path.isfile(path):
            continue

        if fname.lower().endswith(".pdf"):
            text = extract_text_from_pdf(path)
        elif fname.lower().endswith(".docx"):
            text = extract_text_from_docx(path)
        elif fname.lower().endswith(".txt"):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        else:
            continue

        text = clean_text(text)
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata.append({"source": fname, "chunk_id": i, "text": chunk})

    return all_chunks, metadata
