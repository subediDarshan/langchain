from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004')

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
print(scores)
# [0.37574341 0.37946316 0.36264173 0.37905126 0.56206369]
print(list(enumerate(scores)))
# [(0, np.float64(0.37574340881227475)), (1, np.float64(0.379463159564959)), (2, np.float64(0.3626417258509522)), (3, np.float64(0.37905125800258427)), (4, np.float64(0.5620636859095273))]
print(sorted(list(enumerate(scores)),key=lambda x:x[1]))
# [(2, np.float64(0.3626417258509522)), (0, np.float64(0.37574340881227475)), (3, np.float64(0.37905125800258427)), (1, np.float64(0.379463159564959)), (4, np.float64(0.5620636859095273))]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)





