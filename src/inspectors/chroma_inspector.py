from src.vectorstores.chroma_client import ChromaClient


class ChromaInspector:
    """Inspect the contents of the Chroma vector database."""

    def __init__(self):
        self.client = ChromaClient()

    def count(self) -> int:
        return self.client.count()

    def peek(self) -> dict:
        return self.client.collection.peek()
