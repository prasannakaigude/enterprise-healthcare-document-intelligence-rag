"""Grounded answer generation with source citations."""

from dataclasses import dataclass
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

    if not chunks:
        return GroundedAnswer(
            answer="The provided documents do not contain enough information to answer this question.",
            citations=[],
        )

    prompt = build_grounded_prompt(question=question, chunks=chunks)

    if llm_callable:
        answer = llm_callable(prompt)
    else:
        active_llm = llm or create_chat_llm()
        answer = _call_langchain_llm(active_llm, prompt)

    citations = [
        SourceCitation(
            file_name=chunk.file_name,
            page_number=chunk.page_number,
            chunk_id=chunk.chunk_id,
        )
        for chunk in chunks
    ]

    return GroundedAnswer(answer=answer, citations=citations)

