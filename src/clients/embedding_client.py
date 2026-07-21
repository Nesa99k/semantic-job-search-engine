from sentence_transformers import SentenceTransformer


class EmbeddingClient:
    """Generate text embeddings using a SentenceTransformer model."""

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ) -> None:

        self.model = SentenceTransformer(model_name)

        # --------------------------one document ------------------------------
    def create_embedding(self, text: str) -> list[float]:
        embedding = self.model.encode(text, normalize_embeddings=True)
        return embedding.tolist()

        # --------------------------all document ------------------------------

    def create_embeddings(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(
            texts, normalize_embeddings=True, show_progress_bar=True)

        return embeddings.tolist()
