from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

history = [SystemMessage(content="You are AI-Assistant")]

while True:
    user = input("User: ")
    history.append(HumanMessage(content=user))

    if user == "exit":
        break

    ai = model.invoke(history)
    print("AI: ", ai.content)
    history.append(AIMessage(content=ai.content))