from dataclasses import dataclass
from typing import Any


@dataclass
class EmbeddedDocument:
    """Represent a document together with its vector embedding."""
    id: str
    content: str
    metadata: dict[str, Any]
    embedding: list[float]
