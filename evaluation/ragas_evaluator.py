"""RAGAS evaluation helpers for the healthcare RAG platform."""

from dataclasses import dataclass
from typing import Dict, List

from datasets import Dataset


@dataclass(frozen=True)
class RAGASEvaluationExample:
    """One RAGAS evaluation example."""

    question: str
    answer: str
    contexts: List[str]
    ground_truth: str


def build_evaluation_dataset(examples: List[RAGASEvaluationExample]) -> Dataset:
    """Create a Hugging Face Dataset in the format expected by RAGAS."""

    if not examples:
        raise ValueError("At least one evaluation example is required.")

    rows: Dict[str, list] = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": [],
    }

    for example in examples:
        rows["question"].append(example.question)
        rows["answer"].append(example.answer)
        rows["contexts"].append(example.contexts)
        rows["ground_truth"].append(example.ground_truth)

    return Dataset.from_dict(rows)


def sample_evaluation_examples() -> List[RAGASEvaluationExample]:
    """Return a tiny local sample dataset for learning the RAGAS format."""

    return [
        RAGASEvaluationExample(
            question="What should patients monitor for hypertension?",
            answer="Patients should monitor their blood pressure regularly.",
            contexts=[
                "Patients with hypertension should monitor blood pressure regularly."
            ],
            ground_truth="Patients with hypertension should monitor blood pressure regularly.",
        ),
        RAGASEvaluationExample(
            question="Why are follow-up appointments important?",
            answer="Follow-up appointments help clinicians adjust treatment plans.",
            contexts=[
                "Follow-up appointments help clinicians adjust treatment plans."
            ],
            ground_truth="Follow-up appointments help clinicians adjust treatment plans.",
        ),
    ]


def run_ragas_evaluation(dataset: Dataset):
    """Run RAGAS metrics on a prepared dataset.

    This function may call LLMs and embeddings depending on RAGAS configuration.
    Use it after setting local API keys and confirming the dataset is ready.
    """

    try:
        from ragas import evaluate
        from ragas.metrics import answer_relevancy, context_precision, faithfulness
    except ImportError as error:
        raise ImportError(
            "RAGAS is not installed. Install it with `pip install ragas datasets`."
        ) from error

    return evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
        ],
    )

