"""Search the local ChromaDB vector store for relevant chunks."""

from pathlib import Path
import sys
import warnings


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from backend.app.core.settings import get_settings
from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.rag.vector_store import create_openai_embeddings


def main() -> None:
    """Run a semantic search query against local ChromaDB."""

    if len(sys.argv) < 2:
        print('Usage: python3 scripts/search_vector_store.py "your question"')
        return

    query = " ".join(sys.argv[1:])
    settings = get_settings()
    embeddings = create_openai_embeddings(settings)

    results = retrieve_relevant_chunks(
        query=query,
        embeddings=embeddings,
        persist_directory=settings.chroma_db_dir,
        collection_name=settings.chroma_collection_name,
        top_k=settings.retrieval_top_k,
    )

    print(f"Query: {query}")
    print(f"Results found: {len(results)}")

    for index, result in enumerate(results, start=1):
        preview = result.text[:240].replace("\n", " ")
        print(
            f"{index}. {result.file_name} | page {result.page_number} | "
            f"{result.chunk_id} | score {result.score}"
        )
        print(f"   {preview}")


if __name__ == "__main__":
    main()
