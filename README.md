# Semantic Job Search Engine

A semantic search engine for AI-related job postings built with **Python**, **Sentence Transformers**, and **ChromaDB**.

The project converts structured job records into searchable documents, generates vector embeddings, stores them in a vector database, and retrieves the most relevant jobs using semantic similarity combined with metadata filtering.

---

## Features

- Semantic search using sentence embeddings
- Vector database with ChromaDB
- Metadata filtering
  - Country
  - City
  - Industry
  - Category
  - Experience Level
  - Remote Jobs
  - LLM Roles
- Numeric filtering
  - Minimum Salary
  - Maximum Salary
- Clean layered architecture
- Command Line Interface (CLI)

---

## Project Workflow

```text
CSV Dataset
      │
      ▼
CSVLoader
      │
      ▼
DatasetValidator
      │
      ▼
DocumentBuilder
      │
      ▼
Document
      │
      ▼
EmbeddingPipeline
      │
      ▼
EmbeddedDocument
      │
      ▼
ChromaDB
      │
      ▼
Retriever
      │
      ▼
RetrievedDocument
      │
      ▼
Formatter
      │
      ▼
Console Output
```

---

## Project Structure

```text
src/
│
├── analyzers/
├── apps/
├── builders/
├── clients/
├── formatters/
├── indexers/
├── inspectors/
├── loaders/
├── models/
├── pipelines/
├── retrievers/
├── services/
├── validators/
└── vectorstores/
```

---

## Technologies

- Python
- ChromaDB
- Sentence Transformers
- Hugging Face
- Pandas
- Dataclasses

---

## Installation

Clone the repository

```bash
git clone https://github.com/Nesa99k/semantic-job-search-engine.git

cd semantic-job-search-engine
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Index the Dataset

Run

```bash
python -m src.apps.index_jobs
```

This will

- Load the dataset
- Validate records
- Build documents
- Generate embeddings
- Store vectors in ChromaDB

---

## Search Jobs

Run

```bash
python -m src.apps.search_jobs
```

Example

```text
Query:
LLM Engineer

Country:
USA

Minimum Salary:
250000

Remote Only:
Yes
```

---

## Example Output

```text
Distance : 0.3833

Title    : LLM Engineer

Salary   : $354,000

Country  : USA

Location : Boston

Remote   : Fully Remote
```

---

## Architecture

The project follows a layered architecture.

```text
Applications
      │
Services
      │
Retrievers
      │
Embedding + Vector Store
      │
Models
```

Each layer has a single responsibility, making the project easy to maintain and extend.

---

## Future Improvements

- Hybrid Search (Semantic + Keyword)
- Reranking
- Web API (FastAPI)
- Streamlit Interface
- LLM-powered Career Assistant
- Conversation Memory
- Recommendation Explanation

---

## Author

Nesa Karimi

