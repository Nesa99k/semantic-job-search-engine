from dataclasses import dataclass, field
import uuid
from typing import Any


@dataclass
class Document:
    """Represent a searchable text document."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
