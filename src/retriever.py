from sentence_transformers import SentenceTransformer
import faiss, json, numpy as np, os

def load_index(index_dir="index"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    index = faiss.read_index(f"{index_dir}/faiss.index")
    with open(f"{index_dir}/metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    return model, index, metadata

def retrieve(query, top_k=3, index_dir="index"):
    model, index, metadata = load_index(index_dir)
    q_emb = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)

    scores, ids = index.search(q_emb, top_k)
    results = []
    for i, idx in enumerate(ids[0]):
        if idx == -1:
            continue
        results.append({
            "score": float(scores[0][i]),
            "source": metadata[idx]["source"],
            "text": metadata[idx]["text"]
        })
    return results
