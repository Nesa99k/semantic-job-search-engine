from src.models.embedded_document import EmbeddedDocument
from src.vectorstores.chroma_client import ChromaClient


class ChromaIndexer:
    """Store embedded documents into the Chroma vector database."""

    def __init__(self):
        self.client = ChromaClient()

     # ----------------------------------------------------
    def index(self, documents: list[EmbeddedDocument]) -> None:

        ids = []

        contents = []

        metadatas = []

        embeddings = []

        for document in documents:

            ids.append(document.id)

            contents.append(document.content)

            metadatas.append(document.metadata)

            embeddings.append(document.embedding)

        self.client.collection.add(
            ids=ids,

            documents=contents,

            metadatas=metadatas,

            embeddings=embeddings
        )
