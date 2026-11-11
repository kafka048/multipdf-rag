from src.loader import load_pdf

docs = load_pdf("data/vriddha_jan_pension_yojana.pdf")
print(f"Loaded {len(docs)} Documents")
print(f"First Document: {docs[0].page_content}")
print(f"First Document Metadata: {docs[0].metadata}")
print(f"First Document Source: {docs[0].metadata["source"]}")
print(f"First Document Page And Page Label: {docs[0].metadata["page"]} and {docs[0].metadata['page_label']}")
print(f"Document's page labels: {[doc.metadata['page_label'] for doc in docs]}")

