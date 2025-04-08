from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate([
    ("system", "You are ai assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])

chat_history = []

with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

chat_prompt = chat_prompt_template.invoke({"chat_history": chat_history, "query":"My refund status?"})

print(chat_prompt)