from src.clients.embedding_client import EmbeddingClient
from src.models.document import Document
from src.models.embedded_document import EmbeddedDocument


class EmbeddingPipeline:
    """Convert Document objects into EmbeddedDocument objects."""

    def __init__(self):
        self.client = EmbeddingClient()

    def run(self, documents: list[Document]) -> list[EmbeddedDocument]:
        texts = [document.content for document in documents]
        embeddings = self.client.create_embeddings(texts)
        embedded_documents = []
        for document, embedding in zip(documents, embeddings):
            embedded_documents.append(EmbeddedDocument(
                id=document.id,
                content=document.content,
                metadata=document.metadata,
                embedding=embedding
            ))
        return embedded_documents
