from statistics import mean, median
from typing import Any
import tiktoken

from src.models.document import Document


class TokenAnalyzer:
    """
    Analyze token statistics for a collection of documents.
    """

    def __init__(self, model_name: str = "text-embedding-3-small") -> None:
        self.encoding = tiktoken.encoding_for_model(model_name)

    # ----------------------------------------------------------

    def analyze(self, documents: list[Document]) -> dict[str, Any]:
        token_counts = []
        for document in documents:
            tokens = self.encoding.encode(document.content)
            token_counts.append(len(tokens))
        return self._build_statistics(token_counts)

    def _build_statistics(self, token_counts: list[int]) -> dict[str, Any]:
        return {
            "document_count": len(token_counts),

            "minimum_tokens": min(token_counts),

            "maximum_tokens": max(token_counts),

            "average_tokens": round(mean(token_counts), 2),

            "median_tokens": median(token_counts),

        }
