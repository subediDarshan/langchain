from langchain_community.document_loaders import PyPDFLoader

# import requests

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)


# there are several other pdf loaders
# pypdf is used for basic text extraction from pdf
# if we want to extract from scanned pdf or pdf having table we should look for other options
# like UnstrucuredPDFLoader, AmazonTextractPDFLoader, etc



# url = "https://coo24d0qap.ufs.sh/f/gvBqm3evYBDOyGXfrFgXhLwvJ6p0Sc9RkG4FAUM1E3VYPeNr"
# response = requests.get(url)

# with open("document.pdf", "wb") as f:
#     f.write(response.content)


# loader = PyPDFLoader("document.pdf")
# docs = loader.load()

# print(docs)