from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

paper_input = "Attention is all you need"
prompt_template = load_prompt("prompt.json")

chain = prompt_template | model
result = chain.invoke({"paper_name": paper_input})

print(result.content)