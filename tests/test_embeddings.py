from src.splitter import split
from src.loader import load_folder
from src.embeddings import get_embedding_model
from langchain_core.documents import Document  

pages: list[Document] = load_folder("data")
split_pages: list[Document] = split(pages, 1000, 200)
embedding_model = get_embedding_model()

vector = embedding_model.embed_query("When does the scheme come into force?")
print(f"Embedding vector length: {len(vector)}")


texts = [page.page_content for page in split_pages]
vectors = embedding_model.embed_documents(texts)
print(f"Number of vectors: {len(vectors)}")
print(f"Length of each vector: {len(vectors[0]) if vectors else 0}")

vector = vectors[0]  # the first chunk's vector
size = sum(x * x for x in vector) ** 0.5  # square every number, add them up, take the square root
print(size)  # about 1.0 if normalizing is on
