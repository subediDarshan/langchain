from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

load_dotenv()

paper_input = "Attention is all you need"

# prompt_template = PromptTemplate(template="Summarize {paper_name} in 10 words", input_variables=["paper_name"])
prompt_template = load_prompt("prompt.json")

prompt = prompt_template.invoke({"paper_name": paper_input})

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = model.invoke(prompt)

print(result.content)