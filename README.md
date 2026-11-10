# Project 2: Multi-Document RAG Q&A

## What it does

Ask natural-language questions across a set of government scheme PDFs and get an answer grounded in those documents, with the file and page it came from. If the documents do not contain the answer, it says so instead of guessing. Everything runs locally, with no API keys.

## Corpus

Four fictional scheme guideline documents from a fictional state. Three are text PDFs and one is a scan with no text layer, so it needs OCR.

## Pipeline

Load PDFs (OCR for scans), split into chunks, embed, store in Chroma, retrieve the top-k chunks for a question with vector search and keyword search combined, generate an answer with a local LLM.

## Scope

In scope:

- Several PDFs at a time, with the source file and page kept on every chunk
- OCR for scanned pages
- Recursive chunking
- Hybrid search: vector search plus BM25
- A hand-written question set and evaluation, comparing vector-only retrieval with hybrid
- Persistent vector store, so a restart does not re-embed
- One FastAPI endpoint: `POST /ask`

