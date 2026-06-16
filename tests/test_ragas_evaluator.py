import unittest

from datasets import Dataset

from evaluation.ragas_evaluator import (
    RAGASEvaluationExample,
    build_evaluation_dataset,
    sample_evaluation_examples,
)


class RAGASEvaluatorTests(unittest.TestCase):
    def test_build_evaluation_dataset_has_expected_columns(self):
        examples = [
            RAGASEvaluationExample(
                question="What should patients monitor?",
                answer="Patients should monitor blood pressure.",
                contexts=["Patients should monitor blood pressure."],
                ground_truth="Patients should monitor blood pressure.",
            )
        ]

        dataset = build_evaluation_dataset(examples)

        self.assertIsInstance(dataset, Dataset)
        self.assertEqual(len(dataset), 1)
        self.assertEqual(
            dataset.column_names,
            ["question", "answer", "contexts", "ground_truth"],
        )
        self.assertEqual(dataset[0]["question"], "What should patients monitor?")
        self.assertEqual(
            dataset[0]["contexts"],
            ["Patients should monitor blood pressure."],
        )

    def test_build_evaluation_dataset_rejects_empty_examples(self):
        with self.assertRaises(ValueError):
            build_evaluation_dataset([])

    def test_sample_evaluation_examples_are_valid(self):
        examples = sample_evaluation_examples()

        self.assertGreaterEqual(len(examples), 2)
        self.assertTrue(all(example.question for example in examples))
        self.assertTrue(all(example.answer for example in examples))
        self.assertTrue(all(example.contexts for example in examples))
        self.assertTrue(all(example.ground_truth for example in examples))


if __name__ == "__main__":
    unittest.main()
