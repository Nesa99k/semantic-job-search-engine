from src.clients.embedding_client import EmbeddingClient
from src.vectorstores.chroma_client import ChromaClient
from src.models.retrieved_document import RetrievedDocument
from src.models.search_request import SearchRequest


class ChromaRetriever:
    """Retrieve relevant documents from the Chroma vector database."""

    def __init__(self):
        self.client = ChromaClient()
        self.embedding_client = EmbeddingClient()

    def retrieve(
        self,
        request: SearchRequest
    ) -> list[RetrievedDocument]:
        where_filter = self._build_where_filter(request)

        query_embedding = self.embedding_client.create_embedding(
            request.query
        )
        query_kwargs = {
            "query_embeddings": [query_embedding],
            "n_results": request.top_k,
            "include": [
                "documents",
                "metadatas",
                "distances"
            ]
        }

        if where_filter is not None:
            query_kwargs["where"] = where_filter

        results = self.client.collection.query(**query_kwargs)

        retrieved_documents = []

        for i in range(len(results["ids"][0])):

            retrieved_documents.append(

                RetrievedDocument(

                    id=results["ids"][0][i],

                    content=results["documents"][0][i],

                    metadata=results["metadatas"][0][i],

                    distance=results["distances"][0][i]

                )

            )

        return retrieved_documents

    def _build_where_filter(
        self,
        request: SearchRequest
    ) -> dict | None:

        filters = []

    # ---------- Country ----------

        if request.country:

            filters.append(
                {
                    "country": request.country
                }
            )

    # ---------- City ----------

        if request.city:

            filters.append(
                {
                    "city": request.city
                }
            )

    # ---------- Industry ----------

        if request.industry:

            filters.append(
                {
                    "industry": request.industry
                }
            )

    # ---------- Category ----------

        if request.category:

            filters.append(
                {
                    "category": request.category
                }
            )

    # ---------- Experience ----------

        if request.experience_level:

            filters.append(
                {
                    "experience_level": request.experience_level
                }
            )

    # ---------- Remote ----------

        if request.remote_only:

            filters.append(
                {
                    "is_remote_friendly": True
                }
            )

    # ---------- LLM ----------

        if request.is_llm_role is not None:

            filters.append(
                {
                    "is_llm_role": request.is_llm_role
                }
            )

    # ---------- Salary ----------

        salary_filter = {}

        if request.min_salary is not None:

            salary_filter["$gte"] = request.min_salary

        if request.max_salary is not None:

            salary_filter["$lte"] = request.max_salary

        if salary_filter:

            filters.append(
                {
                    "salary": salary_filter
                }
            )

    # ---------- Return ----------

        if len(filters) == 0:

            return None

        if len(filters) == 1:

            return filters[0]

        return {
            "$and": filters
        }
