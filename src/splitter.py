from langchain_text_splitters import RecursiveCharacterTextSplitter  
from langchain_core.documents import Document  

def split(pages: list[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> list[Document]:

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=chunk_overlap, chunk_size=chunk_size       
    )

    split_pages: list[Document] = []

    for page in pages:
        page_chunks:list[str] = text_splitter.split_text(page.page_content)
        page_chunks = [chunk for chunk in page_chunks if chunk.strip()] # remove empty/blank chunks
        for i, chunk in enumerate(page_chunks):
            split_page = Document(
                page_content = chunk,
                metadata = {
                    **page.metadata,
                    "chunk_index": i,
                }
            )
            split_pages.append(split_page)

    return split_pages


