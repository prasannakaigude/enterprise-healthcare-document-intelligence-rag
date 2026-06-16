"""Retrieve relevant chunks and generate a grounded answer."""

from pathlib import Path
import sys
import warnings


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from backend.app.core.settings import get_settings
from backend.app.rag.answer_generator import create_chat_llm, generate_grounded_answer
from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.rag.vector_store import create_openai_embeddings


def main() -> None:
    """Run retrieval and grounded answer generation from the terminal."""

    if len(sys.argv) < 2:
        print('Usage: python3 scripts/answer_question.py "your question"')
        return

    question = " ".join(sys.argv[1:])
    settings = get_settings()
    embeddings = create_openai_embeddings(settings)
    llm = create_chat_llm(settings)

    chunks = retrieve_relevant_chunks(
        query=question,
        embeddings=embeddings,
        persist_directory=settings.chroma_db_dir,
        collection_name=settings.chroma_collection_name,
        top_k=settings.retrieval_top_k,
    )
    grounded_answer = generate_grounded_answer(
        question=question,
        chunks=chunks,
        llm=llm,
    )

    print(f"Question: {question}")
    print("\nAnswer:")
    print(grounded_answer.answer)
    print("\nSources:")

    for citation in grounded_answer.citations:
        print(f"- {citation.file_name}, page {citation.page_number}, {citation.chunk_id}")


if __name__ == "__main__":
    main()

