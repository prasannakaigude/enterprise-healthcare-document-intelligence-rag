import unittest
from unittest.mock import patch

from backend.app.core.settings import Settings, get_settings
from backend.app.rag.answer_generator import (
    build_context,
    build_grounded_prompt,
    build_unique_citations,
    create_chat_llm,
    generate_grounded_answer,
    select_relevant_chunks,
)
from backend.app.rag.retriever import RetrievedChunk


class AnswerGeneratorTests(unittest.TestCase):
    def _sample_chunks(self):
        return [
            RetrievedChunk(
                text="Patients with hypertension should monitor blood pressure regularly.",
                score=0.12,
                file_name="hypertension-guide.pdf",
                page_number=4,
                chunk_id="hypertension-guide.pdf:page-4:chunk-1",
                metadata={"file_name": "hypertension-guide.pdf"},
            ),
            RetrievedChunk(
                text="Follow-up appointments help clinicians adjust treatment plans.",
                score=0.24,
                file_name="care-plan.pdf",
                page_number=2,
                chunk_id="care-plan.pdf:page-2:chunk-1",
                metadata={"file_name": "care-plan.pdf"},
            ),
        ]

    def test_settings_include_chat_model_defaults(self):
        settings = get_settings()

        self.assertEqual(settings.chat_model, "gpt-4o-mini")
        self.assertEqual(settings.chat_temperature, 0.0)

    def test_create_chat_llm_requires_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                create_chat_llm(Settings())

    def test_build_context_includes_source_metadata(self):
        context = build_context(self._sample_chunks())

        self.assertIn("hypertension-guide.pdf", context)
        self.assertIn("Page: 4", context)
        self.assertIn("Chunk ID: hypertension-guide.pdf:page-4:chunk-1", context)
        self.assertIn("blood pressure", context)

    def test_build_grounded_prompt_includes_rules(self):
        prompt = build_grounded_prompt(
            "How should hypertension be monitored?",
            self._sample_chunks(),
        )

        self.assertIn("Answer using only the retrieved source context", prompt)
        self.assertIn("How should hypertension be monitored?", prompt)
        self.assertIn("hypertension-guide.pdf", prompt)

    def test_generate_grounded_answer_uses_fake_llm_and_returns_citations(self):
        def fake_llm(prompt):
            self.assertIn("hypertension-guide.pdf", prompt)
            return (
                "Patients should monitor blood pressure regularly "
                "(hypertension-guide.pdf, page 4)."
            )

        grounded_answer = generate_grounded_answer(
            question="How should hypertension be monitored?",
            chunks=self._sample_chunks(),
            llm_callable=fake_llm,
        )

        self.assertIn("blood pressure", grounded_answer.answer)
        self.assertEqual(len(grounded_answer.citations), 1)
        self.assertEqual(
            grounded_answer.citations[0].file_name,
            "hypertension-guide.pdf",
        )
        self.assertEqual(grounded_answer.citations[0].page_number, 4)

    def test_generate_grounded_answer_deduplicates_citations_by_file_and_page(self):
        chunks = [
            RetrievedChunk(
                text="Water fluoridation improves dental health.",
                score=0.10,
                file_name="public-health.pdf",
                page_number=25,
                chunk_id="public-health.pdf:page-25:chunk-1",
                metadata={},
            ),
            RetrievedChunk(
                text="Water fluoridation is discussed by public health agencies.",
                score=0.11,
                file_name="public-health.pdf",
                page_number=25,
                chunk_id="public-health.pdf:page-25:chunk-2",
                metadata={},
            ),
            RetrievedChunk(
                text="Water fluoridation policy decisions can happen locally.",
                score=0.12,
                file_name="public-health.pdf",
                page_number=25,
                chunk_id="public-health.pdf:page-25:chunk-3",
                metadata={},
            ),
        ]

        grounded_answer = generate_grounded_answer(
            question="Explain water fluoridation.",
            chunks=chunks,
            llm_callable=lambda prompt: "Water fluoridation improves dental health.",
        )

        self.assertEqual(len(grounded_answer.citations), 1)
        self.assertEqual(grounded_answer.citations[0].file_name, "public-health.pdf")
        self.assertEqual(grounded_answer.citations[0].page_number, 25)

    def test_build_unique_citations_keeps_different_pages(self):
        citations = build_unique_citations(
            [
                RetrievedChunk(
                    text="Water fluoridation improves dental health.",
                    score=0.10,
                    file_name="public-health.pdf",
                    page_number=25,
                    chunk_id="public-health.pdf:page-25:chunk-1",
                    metadata={},
                ),
                RetrievedChunk(
                    text="Water quality standards are also discussed.",
                    score=0.12,
                    file_name="public-health.pdf",
                    page_number=26,
                    chunk_id="public-health.pdf:page-26:chunk-1",
                    metadata={},
                ),
            ]
        )

        self.assertEqual(len(citations), 2)
        self.assertEqual([citation.page_number for citation in citations], [25, 26])

    def test_select_relevant_chunks_filters_unrelated_chunks(self):
        relevant_chunks = select_relevant_chunks(
            question="How should hypertension be monitored?",
            chunks=self._sample_chunks(),
        )

        self.assertEqual(len(relevant_chunks), 1)
        self.assertEqual(relevant_chunks[0].file_name, "hypertension-guide.pdf")

    def test_generate_grounded_answer_handles_no_chunks(self):
        grounded_answer = generate_grounded_answer(
            question="What does the document say about discharge?",
            chunks=[],
            llm_callable=lambda prompt: "This should not be called.",
        )

        self.assertIn("could not find enough relevant information", grounded_answer.answer)
        self.assertEqual(grounded_answer.citations, [])

    def test_generate_grounded_answer_guardrails_irrelevant_question(self):
        grounded_answer = generate_grounded_answer(
            question="What is the capital of France?",
            chunks=self._sample_chunks(),
            llm_callable=lambda prompt: "This should not be called.",
        )

        self.assertIn("healthcare documents", grounded_answer.answer)
        self.assertEqual(grounded_answer.citations, [])

    def test_generate_grounded_answer_rejects_empty_question(self):
        with self.assertRaises(ValueError):
            generate_grounded_answer(question=" ", chunks=self._sample_chunks())


if __name__ == "__main__":
    unittest.main()
