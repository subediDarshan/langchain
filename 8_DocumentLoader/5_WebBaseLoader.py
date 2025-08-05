# It uses BeautifulSoup under the hood to parse HTML and extract visible text
# Doesnt handle JS heavy pages well (Use Selenium URL Loader fro that)
# Loads only static content which are in html


from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv



load_dotenv()

# model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

# prompt = PromptTemplate(
#     template='Answer the following question \n {question} from the following text - \n {text}',
#     input_variables=['question','text']
# )

# parser = StrOutputParser()



url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)





# chain = prompt | model | parser

# print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))






