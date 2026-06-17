"""Grounded answer generation with source citations."""

from dataclasses import dataclass
import re
from typing import Callable, List
import os
import warnings


warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from backend.app.core.settings import Settings, get_settings
from backend.app.rag.retriever import RetrievedChunk


LLMCallable = Callable[[str], str]


@dataclass(frozen=True)
class SourceCitation:
    """Citation metadata for one retrieved source chunk."""

    file_name: str
    page_number: int
    chunk_id: str


@dataclass(frozen=True)
class GroundedAnswer:
    """Generated answer and the sources used to ground it."""

    answer: str
    citations: List[SourceCitation]


STOPWORDS = {
    "a",
    "about",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "does",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "policy",
    "say",
    "should",
    "the",
    "this",
    "to",
    "what",
    "when",
    "where",
    "who",
    "why",
    "with",
}


def _content_tokens(text: str) -> set[str]:
    """Return meaningful lowercase tokens for simple relevance checks."""

    tokens = set(re.findall(r"[a-zA-Z][a-zA-Z0-9-]{2,}", text.lower()))
    return {token for token in tokens if token not in STOPWORDS}


def chunk_matches_question(question: str, chunk: RetrievedChunk) -> bool:
    """Check whether a retrieved chunk has basic lexical overlap with the question."""

    question_tokens = _content_tokens(question)

    if not question_tokens:
        return False

    chunk_tokens = _content_tokens(chunk.text)
    return bool(question_tokens.intersection(chunk_tokens))


def select_relevant_chunks(
    question: str,
    chunks: List[RetrievedChunk],
    max_chunks: int = 3,
) -> List[RetrievedChunk]:
    """Keep only chunks that look relevant and avoid exact duplicate chunks."""

    selected_chunks: List[RetrievedChunk] = []
    seen_sources: set[tuple[str, int, str]] = set()

    for chunk in chunks:
        if not chunk_matches_question(question, chunk):
            continue

        source_key = (chunk.file_name, chunk.page_number, chunk.chunk_id)

        if source_key in seen_sources:
            continue

        selected_chunks.append(chunk)
        seen_sources.add(source_key)

        if len(selected_chunks) >= max_chunks:
            break

    return selected_chunks


def build_unique_citations(chunks: List[RetrievedChunk]) -> List[SourceCitation]:
    """Create user-facing citations without repeating the same file/page."""

    citations: List[SourceCitation] = []
    seen_pages: set[tuple[str, int]] = set()

    for chunk in chunks:
        page_key = (chunk.file_name, chunk.page_number)

        if page_key in seen_pages:
            continue

        citations.append(
            SourceCitation(
                file_name=chunk.file_name,
                page_number=chunk.page_number,
                chunk_id=chunk.chunk_id,
            )
        )
        seen_pages.add(page_key)

    return citations


def create_chat_llm(settings: Settings = None) -> ChatOpenAI:
    """Create the real OpenAI chat model client from environment settings."""

    active_settings = settings or get_settings()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY is not set. Create a local .env file or export the "
            "variable before running real OpenAI answer generation."
        )

    return ChatOpenAI(
        model=active_settings.chat_model,
        temperature=active_settings.chat_temperature,
    )


def build_context(chunks: List[RetrievedChunk]) -> str:
    """Format retrieved chunks into citation-aware context for the LLM."""

    context_blocks = []

    for index, chunk in enumerate(chunks, start=1):
        context_blocks.append(
            "\n".join(
                [
                    f"[Source {index}]",
                    f"File: {chunk.file_name}",
                    f"Page: {chunk.page_number}",
                    f"Chunk ID: {chunk.chunk_id}",
                    "Text:",
                    chunk.text,
                ]
            )
        )

    return "\n\n".join(context_blocks)


def build_grounded_prompt(question: str, chunks: List[RetrievedChunk]) -> str:
    """Build the user prompt for grounded answer generation."""

    context = build_context(chunks)

    return f"""Question:
{question}

Retrieved source context:
{context}

Instructions:
- Answer using only the retrieved source context.
- If the context does not contain the answer, say that the provided documents do not contain enough information.
- Include source citations using file name and page number.
"""


def _call_langchain_llm(llm: ChatOpenAI, prompt: str) -> str:
    """Call a LangChain chat model and return text content."""

    response = llm.invoke(
        [
            SystemMessage(
                content=(
                    "You are a careful healthcare document assistant. "
                    "Use only the provided context and cite sources."
                )
            ),
            HumanMessage(content=prompt),
        ]
    )
    return str(response.content)


def generate_grounded_answer(
    question: str,
    chunks: List[RetrievedChunk],
    llm: ChatOpenAI = None,
    llm_callable: LLMCallable = None,
) -> GroundedAnswer:
    """Generate an answer using retrieved chunks as grounded context."""

    if not question.strip():
        raise ValueError("question cannot be empty")

    relevant_chunks = select_relevant_chunks(question=question, chunks=chunks)

    if not relevant_chunks:
        return GroundedAnswer(
            answer=(
                "I could not find enough relevant information in the uploaded "
                "documents to answer this question. Please ask a question that is "
                "covered by the healthcare documents."
            ),
            citations=[],
        )

    prompt = build_grounded_prompt(question=question, chunks=relevant_chunks)

    if llm_callable:
        answer = llm_callable(prompt)
    else:
        active_llm = llm or create_chat_llm()
        answer = _call_langchain_llm(active_llm, prompt)

    citations = build_unique_citations(relevant_chunks)

    return GroundedAnswer(answer=answer, citations=citations)
