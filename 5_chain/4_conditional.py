from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")

class Response(BaseModel):
        response: str = Field(description="Just a one line response")

parser = PydanticOutputParser(pydantic_object=Response)

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback\n {feedback}\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser | (lambda x:x.response)),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser | (lambda x:x.response)),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()