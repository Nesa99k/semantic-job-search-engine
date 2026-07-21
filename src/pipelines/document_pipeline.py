from src.models.job import Job
from src.models.document import Document
from src.builders.document_builder import DocumentBuilder


class DocumentPipeline:
    """Convert the list of Job objects to a list of Document objects."""

    def __init__(self):
        self.builder = DocumentBuilder()

    def run(self, jobs: list[Job]) -> list[Document]:
        documents = []
        for job in jobs:
            document = self.builder.build(job)
            documents.append(document)
        return documents
