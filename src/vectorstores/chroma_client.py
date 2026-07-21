import chromadb
from chromadb import PersistentClient
from pathlib import Path


class ChromaClient:
    """Manage the connection to the Chroma vector database."""

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.client = PersistentClient(
            path=str(BASE_DIR / "vector_db")
        )
        self.collection = self.client.get_or_create_collection(name="jobs")

    def count(self) -> int:

        return self.collection.count()
