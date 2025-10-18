from ingest import load_and_chunk_docs
from indexer import build_faiss_index

def main():
    chunks, metadata = load_and_chunk_docs("data")
    texts = [m["text"] for m in metadata]
    build_faiss_index(texts, metadata, "index")

if __name__ == "__main__":
    main()
