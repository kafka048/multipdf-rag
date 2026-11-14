from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model(model_name: str = "BAAI/bge-m3") -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=model_name,
        encode_kwargs={"normalize_embeddings": True})