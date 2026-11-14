from src.splitter import split
from src.loader import load_folder
from langchain_core.documents import Document  

pages: list[Document] = load_folder("data")
split_pages: list[Document] = split(pages, 1000, 200)

print(f"Loaded {len(pages)} Pages")
print(f"Split into {len(split_pages)} Chunks")
print(f"First Chunk: {split_pages[0].page_content}")
print(f"Last Chunk Metadata: {split_pages[-1].metadata}")
print(f"First Chunk Metadata: {split_pages[0].metadata}")


counts: dict[str, int] = {}  # file name -> number of chunks, starts empty
for page in pages:  # first loop over the PAGES, so every file appears, even the scan
    counts[page.metadata["source_pdf"]] = 0  # set each file's count to 0 to begin with
for chunk in split_pages:  # now loop over the CHUNKS and count them
    counts[chunk.metadata["source_pdf"]] += 1  # add 1 to this chunk's file, safe because every file is already in the dictionary
for file_name, count in counts.items():  # .items() gives each key and its value together
    print(f"{file_name}: {count} chunks")  # one line per file