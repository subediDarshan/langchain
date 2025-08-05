from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)







my_text = """An essay is a piece of writing that presents the author's own argument or perspective on a particular topic, often exploring it in a focused and analytical way. Essays can vary in length, style, and purpose, but they generally include an introduction, a body of supporting paragraphs, and a conclusion. 
Here's a more detailed breakdown:
Definition and Purpose:
An essay is a form of writing that allows the author to express their thoughts, ideas, and arguments on a specific subject. 
It can be used to inform, persuade, analyze, or reflect on a topic. 
Essays are commonly assigned in academic settings to help students develop their writing and critical thinking skills. 
They can also be found in various publications, from literary journals to online platforms, offering diverse perspectives and styles. """

splitted_text = splitter.split_text(my_text)

print(splitted_text)