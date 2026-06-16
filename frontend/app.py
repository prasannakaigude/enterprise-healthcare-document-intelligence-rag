"""Streamlit frontend for the healthcare RAG platform."""

import streamlit as st

from frontend.api_client import (
    BackendAPIError,
    DEFAULT_BACKEND_URL,
    ask_backend,
    list_documents_backend,
    rebuild_vector_store_backend,
)
from frontend.document_upload import DEFAULT_RAW_DATA_DIR, save_uploaded_pdf


st.set_page_config(
    page_title="Healthcare Document Intelligence",
    page_icon="",
    layout="wide",
)

st.title("Enterprise Healthcare Document Intelligence")

backend_url = st.sidebar.text_input("Backend URL", value=DEFAULT_BACKEND_URL)

try:
    available_documents = list_documents_backend(backend_url=backend_url)
except BackendAPIError:
    available_documents = []

document_options = ["All indexed PDFs"] + [
    document["file_name"] for document in available_documents
]
selected_document = st.selectbox("Search scope", options=document_options)
selected_file_name = (
    selected_document if selected_document != "All indexed PDFs" else None
)

uploaded_pdf = st.file_uploader("Upload a healthcare PDF", type=["pdf"])

if uploaded_pdf is not None:
    try:
        saved_path = save_uploaded_pdf(uploaded_pdf)
    except (OSError, ValueError) as error:
        st.error(str(error))
    else:
        st.success(f"Saved to {saved_path.relative_to(DEFAULT_RAW_DATA_DIR.parent.parent)}")
        with st.spinner("Processing PDF and updating the vector store..."):
            try:
                indexing_result = rebuild_vector_store_backend(backend_url=backend_url)
            except BackendAPIError as error:
                st.error(str(error))
                st.info("The PDF was saved, but it is not searchable until indexing succeeds.")
            else:
                st.success(
                    "Ready to search: indexed {chunks_created} chunks from {pages} pages.".format(
                        chunks_created=indexing_result.get("chunks_created", 0),
                        pages=indexing_result.get("pdf_pages_parsed", 0),
                    )
                )
                st.rerun()

st.subheader("Demo Questions")
demo_questions = [
    "What does the policy say about prior authorization?",
    "How should member communication be documented?",
    "What privacy rule is emphasized?",
]
demo_columns = st.columns(len(demo_questions))

for column, demo_question in zip(demo_columns, demo_questions):
    if column.button(demo_question, use_container_width=True):
        st.session_state["question"] = demo_question

question = st.text_area(
    "Ask a question",
    key="question",
    placeholder="What does the document say about discharge instructions?",
    height=120,
)

ask_clicked = st.button("Ask", type="primary")

if ask_clicked:
    if not question.strip():
        st.warning("Enter a question before submitting.")
    else:
        with st.spinner("Searching documents and generating an answer..."):
            try:
                result = ask_backend(
                    question=question,
                    backend_url=backend_url,
                    file_name=selected_file_name,
                )
            except (BackendAPIError, ValueError) as error:
                st.error(str(error))
            else:
                st.subheader("Answer")
                st.write(result.get("answer", ""))

                citations = result.get("citations", [])
                st.subheader("Sources")

                if not citations:
                    st.info("No citations returned.")
                else:
                    for citation in citations:
                        st.markdown(
                            "- **{file_name}**, page {page_number}".format(
                                file_name=citation.get("file_name", "unknown"),
                                page_number=citation.get("page_number", "unknown"),
                            )
                        )
