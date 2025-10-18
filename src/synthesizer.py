import textwrap

def simple_summarize(results):
    """Fallback summarizer without LLM (just extracts sentences)."""
    seen = set()
    unique_sentences = []
    for r in results:
        for s in r["text"].split(". "):
            s = s.strip()
            if len(s) > 25 and s not in seen:
                seen.add(s)
                unique_sentences.append(s)
    answer = ". ".join(unique_sentences[:5])
    sources = ", ".join(sorted(set(r["source"] for r in results)))
    return f"{answer}\n\n📚 Sources: {sources}"


def llm_summarize(results, query):
    """Use Ollama (local model) to generate a grounded answer."""
    import ollama

    context = "\n\n".join(
        [f"Source: {r['source']}\nContent: {r['text']}" for r in results]
    )

    prompt = f"""
You are a precise assistant for Nightingale Healthcare Technologies.
Using only the following excerpts, answer the user’s question clearly and concisely.
Include a final 'Sources:' line listing which documents you used.

Question: {query}

Excerpts:
{context}
"""

    try:
        response = ollama.chat(
            model="phi3",  # You can change to mistral, phi3, etc.
            messages=[
                {"role": "system", "content": "Answer using only the provided excerpts."},
                {"role": "user", "content": prompt},
            ],
        )
        return response["message"]["content"].strip()

    except Exception as e:
        return f"[Ollama Error] {e}\n\n{simple_summarize(results)}"
