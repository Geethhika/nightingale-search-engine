try:
    from sentence_transformers import SentenceTransformer
except Exception as e:
    raise ImportError(
        "The package 'sentence-transformers' is not installed or could not be imported. "
        "Install it with: pip install -U sentence-transformers"
    ) from e

import faiss
import numpy as np
import os, pickle, json

def build_faiss_index(chunks, metadata, save_dir="index"):
    os.makedirs(save_dir, exist_ok=True)

    print("🔹 Loading embedding model (this may take a moment)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("🔹 Encoding chunks...")
    embeddings = model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)

    # Normalize for cosine similarity
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # inner product for cosine
    index.add(embeddings)

    print(f"✅ Indexed {len(chunks)} chunks")

    faiss.write_index(index, f"{save_dir}/faiss.index")

    with open(f"{save_dir}/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"📦 Saved index and metadata to {save_dir}/")
