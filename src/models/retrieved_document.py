from dataclasses import dataclass
from typing import Any


@dataclass
class RetrievedDocument:
    """Represent a document retrieved from the vector database."""
    id: str
    content: str
    metadata: dict[str, Any]
    distance: float
