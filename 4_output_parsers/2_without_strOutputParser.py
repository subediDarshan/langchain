# wanted workflow
# create detai report from model and pass the report and generate 5 line summary of that report

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)





