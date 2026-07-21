from src.models.search_request import SearchRequest
from src.services.search_service import SearchService
from src.formatters.result_formatter import ResultFormatter


def main():

    print("\nSemantic Job Search Engine")
    print("-" * 40)

    query = input("Query: ").strip()

    country = input("Country (optional): ").strip()

    industry = input("Industry (optional): ").strip()

    category = input("Category (optional): ").strip()

    experience = input("Experience Level (optional): ").strip()

    min_salary = input("Minimum Salary (optional): ").strip()

    max_salary = input("Maximum Salary (optional): ").strip()

    remote = input("Remote only? (y/n): ").strip().lower()

    llm = input("LLM Role only? (y/n): ").strip().lower()

    top_k = input("Top K Results (default=5): ").strip()

    request = SearchRequest(

        query=query,

        country=country or None,

        industry=industry or None,

        category=category or None,

        experience_level=experience or None,

        min_salary=float(min_salary) if min_salary else None,

        max_salary=float(max_salary) if max_salary else None,

        remote_only=(remote == "y"),

        is_llm_role=True if llm == "y" else None,

        top_k=int(top_k) if top_k else 5

    )

    service = SearchService()

    formatter = ResultFormatter()

    documents = service.search(request)

    formatter.print_results(documents)


if __name__ == "__main__":
    main()
