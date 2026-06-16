"""Streamlit frontend for the healthcare RAG platform."""

import streamlit as st

from frontend.api_client import BackendAPIError, DEFAULT_BACKEND_URL, ask_backend


st.set_page_config(
    page_title="Healthcare Document Intelligence",
    page_icon="",
    layout="wide",
)

st.title("Enterprise Healthcare Document Intelligence")

backend_url = st.sidebar.text_input("Backend URL", value=DEFAULT_BACKEND_URL)

question = st.text_area(
    "Ask a question",
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
                result = ask_backend(question=question, backend_url=backend_url)
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
                            "- **{file_name}**, page {page_number}  \n"
                            "`{chunk_id}`".format(
                                file_name=citation.get("file_name", "unknown"),
                                page_number=citation.get("page_number", "unknown"),
                                chunk_id=citation.get("chunk_id", "unknown"),
                            )
                        )

