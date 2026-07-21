from src.models.retrieved_document import RetrievedDocument


class ResultFormatter:
    """Format and display retrieved search results in a user-friendly layout."""

    def print_results(
        self,
        documents: list[RetrievedDocument]
    ) -> None:

        if len(documents) == 0:

            print("\nNo jobs found.\n")
            return

        print(f"\nFound {len(documents)} matching jobs\n")

        for index, doc in enumerate(documents, start=1):

            metadata = doc.metadata

            print("=" * 70)

            print(f"{index}. {metadata['title']}")

            print()

            print(
                f"📍 Location      : {metadata['city']}, {metadata['country']}")

            print(f"🏭 Industry      : {metadata['industry']}")

            print(f"💼 Category      : {metadata['category']}")

            print(f"📈 Experience    : {metadata['experience_level']}")

            print(f"💰 Salary        : ${metadata['salary']:,.0f}")

            print(f"🏠 Remote        : {metadata['remote_work']}")

            print(f"🤖 LLM Role      : {metadata['is_llm_role']}")

            print(f"📏 Distance      : {doc.distance:.4f}")

            print()

            print(doc.content)

            print()
