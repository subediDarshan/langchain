# schema of json is decided by the llm only
# even if mentioned in the prompt, still uncertain

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me name, age, city of fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({})

result = model.invoke(prompt)

json_output = parser.parse(result.content)

print(json_output)

# chain = template | model | parser

# result = chain.invoke({})

# print(result)
