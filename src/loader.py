from langchain_community.document_loaders import PyPDFLoader  
from langchain_core.documents import Document  
from pathlib import Path # python's tool to treat a text like data as actual folder path


def load_pdf(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path)
    return loader.load()


def load_folder(folder_path: str) -> list[Document]: # takes a folder, returns all pages from all its PDFs
    all_pages: list[Document] = [] # intially an empty list, the pile every page will be added to
    for pdf_path in sorted(Path(folder_path).glob("*.pdf")): # for each path object 
        pages = load_pdf(str(pdf_path)) # load the pdf
        for page in pages: # for each page in the pdf, add the source file name to its metadata
            page.metadata["source_pdf"] = pdf_path.name
        all_pages.extend(pages) # add all the pages to the pile
    return all_pages



