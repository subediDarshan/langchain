from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are expert on {domain}"),
    ("human", "Explain about {topic}"),
])

chat_prompt = chat_template.invoke({"domain": "Computer Science", "topic": "Arrays"})

print(chat_prompt)