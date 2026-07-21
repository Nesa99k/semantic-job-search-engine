from pathlib import Path

from src.loaders.csv_loader import CSVLoader
from src.validators.dataset_validator import DatasetValidator
from src.pipelines.document_pipeline import DocumentPipeline
from src.pipelines.embedding_pipeline import EmbeddingPipeline
from src.indexers.chroma_indexer import ChromaIndexer
from src.inspectors.chroma_inspector import ChromaInspector

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATASET_PATH = (
    BASE_DIR
    / "data"
    / "raw"
    / "ai_jobs_market_2025_2026.csv"
)

loader = CSVLoader(DATASET_PATH)

jobs = loader.load()

validator = DatasetValidator()

validator.validate(jobs)

print(f"Dataset loaded successfully: {len(jobs)} jobs")

document_pipeline = DocumentPipeline()

documents = document_pipeline.run(jobs)

embedding_pipeline = EmbeddingPipeline()

embedded_documents = embedding_pipeline.run(documents)

print(f"Embedded documents: {len(embedded_documents)}")

print(type(embedded_documents[0]))

print(len(embedded_documents[0].embedding))

indexer = ChromaIndexer()

indexer.index(embedded_documents)

print("Vector database created successfully.")

print(

    f"Indexed documents: {indexer.client.count()}"

)

inspector = ChromaInspector()

print(inspector.count())

print(inspector.peek())
