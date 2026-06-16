"""End-to-end RAG pipeline orchestration."""

from backend.app.core.settings import Settings, get_settings
from backend.app.rag.answer_generator import GroundedAnswer, create_chat_llm, generate_grounded_answer
from backend.app.rag.retriever import retrieve_relevant_chunks
from backend.app.rag.vector_store import create_openai_embeddings


def answer_question(question: str, settings: Settings = None) -> GroundedAnswer:
    """Retrieve relevant chunks and generate a grounded answer."""

    active_settings = settings or get_settings()
    embeddings = create_openai_embeddings(active_settings)
    llm = create_chat_llm(active_settings)

    chunks = retrieve_relevant_chunks(
        query=question,
        embeddings=embeddings,
        persist_directory=active_settings.chroma_db_dir,
        collection_name=active_settings.chroma_collection_name,
        top_k=active_settings.retrieval_top_k,
    )

    return generate_grounded_answer(
        question=question,
        chunks=chunks,
        llm=llm,
    )

