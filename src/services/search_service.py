from src.models.retrieved_document import RetrievedDocument
from src.models.search_request import SearchRequest
from src.retrievers.chroma_retriever import ChromaRetriever


class SearchService:
    """Coordinate the document retrieval process."""

    def __init__(self):
        self.retriever = ChromaRetriever()

    def search(
        self,
        request: SearchRequest
    ) -> list[RetrievedDocument]:

        return self.retriever.retrieve(request)
