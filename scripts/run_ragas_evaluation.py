"""Run a small RAGAS evaluation example."""

from pathlib import Path
import sys
import warnings


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

from evaluation.ragas_evaluator import (
    build_evaluation_dataset,
    run_ragas_evaluation,
    sample_evaluation_examples,
)


def main() -> None:
    """Build a sample RAGAS dataset and show how evaluation runs."""

    dataset = build_evaluation_dataset(sample_evaluation_examples())

    print(f"Evaluation examples: {len(dataset)}")
    print("Dataset columns:", ", ".join(dataset.column_names))
    print(
        "RAGAS evaluation may call an LLM. Add local API keys before running "
        "real metric evaluation."
    )

    if "--run" not in sys.argv:
        print("Dry run only. Use `python3 scripts/run_ragas_evaluation.py --run` to evaluate.")
        return

    results = run_ragas_evaluation(dataset)
    print(results)


if __name__ == "__main__":
    main()
