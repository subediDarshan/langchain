from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

for document in docs:
    print(document.metadata) # firslty loads all in memory and then print at once


# if many pdfs are there then it takes more time and consumes more RAM
# to solve this we have lazy loader
# It return a generator of Document objects
# Documents are not all loaded at once, they are fetched one at a time as needed

lazyDocs = loader.lazy_load()

for document in lazyDocs:
    print(document.metadata) # loads one document prints it and removes it from ram and then loads another doc