from retriever import retrieve
from synthesizer import llm_summarize, simple_summarize
from rich.console import Console

console = Console()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Nightingale Knowledge Engine CLI")
    parser.add_argument("query", type=str, help="Your question")
    parser.add_argument("--simple", action="store_true", help="Use simple summarizer instead of LLM")
    parser.add_argument("--topk", type=int, default=4, help="Number of chunks to retrieve")
    args = parser.parse_args()

    console.print("[bold cyan]🔎 Retrieving relevant information...[/bold cyan]")
    results = retrieve(args.query, top_k=args.topk)
    if not results:
        console.print("[red]No relevant information found.[/red]")
        return

    if args.simple:
        answer = simple_summarize(results)
    else:
        console.print("[bold magenta]🤖 Generating answer with Ollama...[/bold magenta]")
        answer = llm_summarize(results, args.query)

    console.print("\n[bold green]💡 Final Answer:[/bold green]\n")
    console.print(answer)

if __name__ == "__main__":
    main()
