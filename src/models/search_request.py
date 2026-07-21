from dataclasses import dataclass


@dataclass
class SearchRequest:
    """Represent a semantic search request."""

    # ---------- Semantic Search ----------

    query: str

    top_k: int = 5

    # ---------- Location ----------

    country: str | None = None

    city: str | None = None

    # ---------- Job ----------

    category: str | None = None

    industry: str | None = None

    # ---------- Experience ----------

    experience_level: str | None = None

    # ---------- Salary ----------

    min_salary: float | None = None

    max_salary: float | None = None

    # ---------- Remote ----------

    remote_only: bool = False

    # ---------- AI ----------

    is_llm_role: bool | None = None
