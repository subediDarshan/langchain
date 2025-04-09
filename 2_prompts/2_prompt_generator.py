from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt_template = PromptTemplate(template="Summarize {paper_name} in 10 words", input_variables=["paper_name"])

prompt_template.save("prompt.json")